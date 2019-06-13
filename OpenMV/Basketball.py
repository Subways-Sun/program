# 色块监测 例子
#
# 这个例子展示了如何通过find_blobs()函数来查找图像中的色块
# 这个例子查找的颜色是深绿色

import sensor, image, time
from pyb import UART


# 找到最大的色块
def find_max(blobs):
    max_size = 0
    for blob in blobs:
        if blob.pixels() > max_size:
            max_blob = blob
            max_size = blob.pixels()

    return max_blob


# 颜色追踪的例子，一定要控制环境的光，保持光线是稳定的。
green_threshold   = (0,   90,  20,   80,   0,   80)
#设置绿色的阈值，括号里面的数值分别是L A B 的最大值和最小值（minL, maxL, minA,
# maxA, minB, maxB），LAB的值在图像左侧三个坐标图中选取。如果是灰度图，则只需
#设置（min, max）两个数字即可。

sensor.reset() # 初始化摄像头
sensor.set_pixformat(sensor.RGB565) # 格式为 RGB565.
sensor.set_framesize(sensor.QQVGA) # 使用 QQVGA 速度快一些
sensor.skip_frames(10) # 跳过10帧，使新设置生效
sensor.set_auto_whitebal(False)
#关闭白平衡。白平衡是默认开启的，在颜色识别中，一定要关闭白平衡。
clock = time.clock() # 追踪帧率

uart = UART(3, 250000) # 打开串口

senddat = 0
nc = 0

while(True):
    if (uart.any() > 0): # 有命令到来就解析命令，否则保持上一次状态
        ch = uart.readchar()
        if (ch == 48):   # 字符'0'
            senddat = 0     # 不发送数据

        if (ch == 49):   # 字符'1'
            senddat = 1     # 发送数据

    #print(ch)

    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # 从感光芯片获得一张图像

    blobs = img.find_blobs([green_threshold])
    #find_blobs(thresholds, invert=False, roi=Auto),thresholds为颜色阈值，
    #是一个元组，需要用括号［ ］括起来。invert=1,反转颜色阈值，invert=False默认
    #不反转。roi设置颜色识别的视野区域，roi是一个元组， roi = (x, y, w, h)，代表
    #从左上顶点(x,y)开始的宽为w高为h的矩形区域，roi不设置的话默认为整个图像视野。
    #这个函数返回一个列表，[0]代表识别到的目标颜色区域左上顶点的x坐标，［1］代表
    #左上顶点y坐标，［2］代表目标区域的宽，［3］代表目标区域的高，［4］代表目标
    #区域像素点的个数，［5］代表目标区域的中心点x坐标，［6］代表目标区域中心点y坐标，
    #［7］代表目标颜色区域的旋转角度（是弧度值，浮点型，列表其他元素是整型），
    #［8］代表与此目标区域交叉的目标个数，［9］代表颜色的编号（它可以用来分辨这个
    #区域是用哪个颜色阈值threshold识别出来的）。
    if blobs:
    #如果找到了目标颜色

        b = find_max(blobs)
        # Draw a rect around the blob.
        img.draw_rectangle(b[0:4]) # rect
        #用矩形标记出目标颜色区域
        img.draw_cross(b[5], b[6]) # cx, cy
        #在目标颜色区域的中心画十字形标记
        # strxy = "(%d,%d)" % (b[5], b[6])
        # print(strxy)
        # uart.write(strxy) # 发送目标物体的坐标


        if (senddat == 1):
            strX = "(%d)" % (b[5])
            print(strX)
            uart.write(strX) # 发送目标物体的x坐标

        time.sleep(50)

    #print(clock.fps()) # 注意: 你的OpenMV连到电脑后帧率大概为原来的一半如果断开电脑，帧率会增加

