import sensor, image, time
from pyb import UART
def find_max(blobs):
    max_size = 0
    for blob in blobs:
        if blob.pixels() > max_size:
            max_blob = blob
            max_size = blob.pixels()
    return max_blob
green_threshold   = (20,   70,   50,   80,   10,   60)
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(10)
sensor.set_auto_whitebal(False)
clock = time.clock()
uart = UART(3, 250000)
senddat = 0
nc = 0
while(True):
    if (uart.any() > 0):
        ch = uart.readchar()
        if (ch == 48):
            senddat = 0
        if (ch == 49):
            senddat = 1
    clock.tick()
    img = sensor.snapshot()
    blobs = img.find_blobs([green_threshold])
    if blobs:
        b = find_max(blobs)
        img.draw_rectangle(b[0:4])
        img.draw_cross(b[5], b[6])
        if (senddat == 1):
            strX = "(%d)" % (b[5])
            print(strX)
            uart.write(strX)
        time.sleep(50)
