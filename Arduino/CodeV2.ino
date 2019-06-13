// Arduino 1.8.5
// 篮球发明

#include <Servo.h>
#define Servo_pinPush   8  // 控制上弹
#define Servo_pinLR     9  // 控制左右旋转的舵机
#define Servo_pinUD     10 // 控制上下摆动的舵机

#define MotorV    3   // 马达速度
#define MotorA    5   // 引脚1
#define MotorB    4   // 引脚2

#define Pin_Trig  7 // 定义超声波信号发出接口
#define Pin_Echo  6 // 定义超声波信号接收接口

Servo servoPush;    // 控制上弹
Servo servoLR;      // 控制左右旋转的舵机
Servo servoUD;      // 控制上下摆动的舵机

// 舵机当前角度
int g_CurangleLR = 90;
int g_CurangleUD = 90;

// 中心左边是(80,60)
#define XO  80

char buf[4] = {0, 0, 0, 0};
int g_CurX = XO; // 目标在视野中的当前X坐标
int g_cls = 0;   // 清理接收缓存

void setup()
{
    // 上电等待3秒钟
    delay(1000);
    delay(1000);
    delay(1000);
    
    // 初始化串口,用于与视觉模块进行通信
    Serial.begin(250000);

    // 初始化马达引脚
    pinMode(MotorA, OUTPUT);  // 引脚A
    pinMode(MotorB, OUTPUT);  // 引脚B
    analogWrite(MotorV, 0);   // 速度控制

    // 初始化舵机
    servoLR.attach(Servo_pinLR);
    servoUD.attach(Servo_pinUD);
    servoPush.attach(Servo_pinPush);

    servoLR.write(90);
    servoUD.write(90);
    servoPush.write(90);

    // 初始化距离传感器
    pinMode(Pin_Echo, INPUT);
    pinMode(Pin_Trig, OUTPUT);

    NeedX(1);
}

void loop()
{
    //Serial.println(GetDistance());
    //delay(1000);
    #if 1
    if (g_cls == 0)
    {
        GetX();
    }
    else
    {
        if (Serial.available() > 0)
        {
            Serial.read();
        }
        else
        {
            g_cls = 0;
            NeedX(1);
        }
    }
    #endif
}

// 获取目标的x坐标
void GetX()
{
    char c;
    static int i = 0;
    static int count = 0;
    if (Serial.available() > 0)
    {
        c = Serial.read();
        if (c == '(')
        {
            i = 0;
            buf[0] = 0;
            buf[1] = 0;
            buf[2] = 0;
            buf[3] = 0;
        }
        else if (c == ')')
        {
            String s = String(buf);
            g_CurX = s.toInt();

            // 正负10个点以内
            if (abs(g_CurX - XO) < 10)
            {
                count++;
                // 连续检测15次位置保持不变
                if (count >= 15)
                {
                    int s = 0;
                    int v = 0;
                    NeedX(0);// 停止数据发送

                    // 距离判读
                    s = GetDistance();
                    v = map(s, 0, 100, 80, 150);

                    // 角度修正
                    g_CurangleLR -= 2;
                    if (g_CurangleLR < 0)
                    {
                        g_CurangleLR = 0;
                    }
                    servoLR.write(g_CurangleLR);
                    // 角度修正
                
                    // 配置俯仰
                    servoUD.write(map(s, 0, 100, 90, 100));
                    delay(1000);
                    
                    // 配置速度
                    digitalWrite(MotorA, HIGH);
                    digitalWrite(MotorB, LOW);
                    analogWrite(MotorV, v);   // 速度控制
                    delay(1500);

                    // 发射
                    servoPush.write(65);// 推入
                    delay(500);
                    servoPush.write(90);// 回位

                    // 停车
                    digitalWrite(MotorA, LOW);
                    digitalWrite(MotorB, LOW);
                    analogWrite(MotorV, 0);   // 速度控制
    
                    // 清空接收缓存区
                    g_cls = 1;
                    count = 0;

                    delay(3000);
                }
            }
            // 目标在视野中偏右，舵机需要向右旋转
            else if (g_CurX > XO)
            {
                g_CurangleLR -= 4;
                if (g_CurangleLR < 0)
                {
                    g_CurangleLR = 0;
                }
                servoLR.write(g_CurangleLR);
                // delay(10);
                count = 0;
            }
            // 目标在视野中偏左，舵机需要向左旋转
            else if (g_CurX < XO)
            {
                g_CurangleLR += 4;
                if (g_CurangleLR > 180)
                {
                    g_CurangleLR = 180;
                }
                servoLR.write(g_CurangleLR);
                // delay(10);
                count = 0;
            }
            else
            {
                count = 0;
            }
        }
        else
        {
            buf[i++] = c;
        }
    }
}

void NeedX(int b)
{
    if (b)
    {
        // 需要x坐标
        Serial.write('1');
    }
    else
    {
        // 不需要x坐标
        Serial.write('0');
    }
}

int GetDistance()
{
    int distance = 0;
    digitalWrite(Pin_Trig, LOW);  // 使发出发出超声波信号接口低电平2μs
    delayMicroseconds(2);
    digitalWrite(Pin_Trig, HIGH); // 使发出发出超声波信号接口高电平10μs，这里是至少10μs
    delayMicroseconds(45);
    digitalWrite(Pin_Trig, LOW);  // 保持发出超声波信号接口低电平
    distance = pulseIn(Pin_Echo, HIGH); // 读出脉冲时间
    distance = distance * 1.03;
    return ((distance * 34000/1000000) / 2); // 将脉冲时间转化为距离（单位：厘米）
}

