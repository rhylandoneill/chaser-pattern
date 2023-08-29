import time
import board
import digitalio

led0 = digitalio.DigitalInOut(board.GP0)
led0.direction = digitalio.Direction.OUTPUT
led1 = digitalio.DigitalInOut(board.GP1)
led1.direction = digitalio.Direction.OUTPUT
led2 = digitalio.DigitalInOut(board.GP2)
led2.direction = digitalio.Direction.OUTPUT
led3 = digitalio.DigitalInOut(board.GP3)
led3.direction = digitalio.Direction.OUTPUT
led4 = digitalio.DigitalInOut(board.GP4)
led4.direction = digitalio.Direction.OUTPUT
led5 = digitalio.DigitalInOut(board.GP5)
led5.direction = digitalio.Direction.OUTPUT
led6 = digitalio.DigitalInOut(board.GP6)
led6.direction = digitalio.Direction.OUTPUT
led7 = digitalio.DigitalInOut(board.GP7)
led7.direction = digitalio.Direction.OUTPUT
led8 = digitalio.DigitalInOut(board.GP8)
led8.direction = digitalio.Direction.OUTPUT
led9 = digitalio.DigitalInOut(board.GP9)
led9.direction = digitalio.Direction.OUTPUT
led10 = digitalio.DigitalInOut(board.GP10)
led10.direction = digitalio.Direction.OUTPUT
led11 = digitalio.DigitalInOut(board.GP11)
led11.direction = digitalio.Direction.OUTPUT
led12 = digitalio.DigitalInOut(board.GP12)
led12.direction = digitalio.Direction.OUTPUT
led13 = digitalio.DigitalInOut(board.GP13)
led13.direction = digitalio.Direction.OUTPUT
led14 = digitalio.DigitalInOut(board.GP14)
led14.direction = digitalio.Direction.OUTPUT
led15 = digitalio.DigitalInOut(board.GP15)
led15.direction = digitalio.Direction.OUTPUT
led16 = digitalio.DigitalInOut(board.GP16)
led16.direction = digitalio.Direction.OUTPUT
led17 = digitalio.DigitalInOut(board.GP17)
led17.direction = digitalio.Direction.OUTPUT
led18 = digitalio.DigitalInOut(board.GP18)
led18.direction = digitalio.Direction.OUTPUT
led19 = digitalio.DigitalInOut(board.GP19)
led19.direction = digitalio.Direction.OUTPUT
led20 = digitalio.DigitalInOut(board.GP20)
led20.direction = digitalio.Direction.OUTPUT
led21 = digitalio.DigitalInOut(board.GP21)
led21.direction = digitalio.Direction.OUTPUT
led22 = digitalio.DigitalInOut(board.GP22)
led22.direction = digitalio.Direction.OUTPUT
led23 = digitalio.DigitalInOut(board.GP23)
led23.direction = digitalio.Direction.OUTPUT
led24 = digitalio.DigitalInOut(board.GP24)
led24.direction = digitalio.Direction.OUTPUT
led25 = digitalio.DigitalInOut(board.GP25)
led25.direction = digitalio.Direction.OUTPUT
led26 = digitalio.DigitalInOut(board.GP26)
led26.direction = digitalio.Direction.OUTPUT
led27 = digitalio.DigitalInOut(board.GP27)
led27.direction = digitalio.Direction.OUTPUT
led28 = digitalio.DigitalInOut(board.GP28)
led28.direction = digitalio.Direction.OUTPUT

while True:
    led0.value = True
    time.sleep(.5)
    led0.value = False
    led1.value = True
    time.sleep(.5)
    led1.value = False
    led2.value = True
    time.sleep(.5)
    led2.value = False
    led3.value = True
    time.sleep(.5)
    led3.value = False
    led4.value = True
    time.sleep(.5)
    led4.value = False
    led5.value = True
    time.sleep(.5)
    led5.value = False
    led6.value = True
    time.sleep(.5)
    led6.value = False
    led7.value = True
    time.sleep(.5)
    led7.value = False
    led8.value = True
    time.sleep(.5)
    led8.value = False
    led9.value = True
    time.sleep(.5)
    led9.value = False
    led10.value = True
    time.sleep(.5)
    led10.value = False
    led11.value = True
    time.sleep(.5)
    led11.value = False
    led12.value = True
    time.sleep(.5)
    led12.value = False
    led13.value = True
    time.sleep(.5)
    led13.value = False
    led14.value = True
    time.sleep(.5)
    led14.value = False
    led15.value = True
    time.sleep(.5)
    led15.value = False
    led16.value = True
    time.sleep(.5)
    led16.value = False
    led17.value = True
    time.sleep(.5)
    led17.value = False
    led18.value = True
    time.sleep(.5)
    led18.value = False
    led19.value = True
    time.sleep(.5)
    led19.value = False
    led20.value = True
    time.sleep(.5)
    led20.value = False
    led21.value = True
    time.sleep(.5)
    led21.value = False
    led22.value = True
    time.sleep(.5)
    led22.value = False
    led23.value = True
    time.sleep(.5)
    led23.value = False
    led24.value = True
    time.sleep(.5)
    led24.value = False
    led25.value = True
    time.sleep(.5)
    led25.value = False
    led26.value = True
    time.sleep(.5)
    led26.value = False
    led27.value = True
    time.sleep(.5)
    led27.value = False
    led28.value = True
    time.sleep(.5)
    led28.value = False

