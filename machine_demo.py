import machine
print(machine.freq())  #125000000
print(machine.freq() * 1.0/ (1000*1000))  #125.0
help(machine)
print(machine.__name__)
print(machine.unique_id()) # b"\xe6`\x10\xb6C,0'" #Returns a byte string with a unique identifier of a board/SoC

import os
print(os.uname())
print(os.uname().release)  #check the software version

import os
print(os.uname())
print(os.uname().release)  ##check the software version
print(os.getcwd()) #Get the current directory
print(os.listdir())
#print(os.mkdir('new_directoryfrompYthon'))
#print(os.listdir())
#print(os.remove('analogdigitalconversion.py'))
#print(os.listdir())
#print(os.remove('new_directoryfrompYthon'))
#print(os.listdir())
#print(os.rename('/newdatafile.txt', '/new_name_for_datafile.txt'))
#print(os.listdir())
print(os.stat('/new_name_for_datafile.txt'))  #Get the status of a file or directory.
print(os.statvfs('/new_name_for_datafile.txt'))  #Get the status of a file system


        # f_bsize – file system block size
        # f_frsize – fragment size
        # f_blocks – size of fs in f_frsize units
        # f_bfree – number of free blocks
        # f_bavail – number of free blocks for unpriviliged users
        # f_files – number of inodes
        # f_ffree – number of free inodes
        # f_favail – number of free inodes for unpriviliged users
        # f_flag – mount flags
        # f_namemax – maximum filename length

import os
import uos

print(os.uname())
#print(uos.random(100))
print(os.uname().release)  ##check the software version
print(os.getcwd()) #Get the current directory
print(os.listdir())
#print(os.mkdir('new_directoryfrompYthon'))
#print(os.listdir())
#print(os.remove('analogdigitalconversion.py'))
#print(os.listdir())
#print(os.remove('new_directoryfrompYthon'))
#print(os.listdir())
#print(os.rename('/newdatafile.txt', '/new_name_for_datafile.txt'))
#print(os.listdir())
print(os.stat('/new_name_for_datafile.txt'))  #Get the status of a file or directory.
fileystem_status = os.statvfs('/new_name_for_datafile.txt')
print(fileystem_status)  #Get the status of a file system (4096, 4096, 352, 328, 328, 0, 0, 0, 0, 255)

print("file system block size: {} * size of fs in f_frsize units {} = {}".format(fileystem_status[0], fileystem_status[2], fileystem_status[0] * fileystem_status[2] ))

        # f_bsize – file system block size            4096
        # f_frsize – fragment size                    4096
        # f_blocks – size of fs in f_frsize units     352
        # f_bfree – number of free blocks
        # f_bavail – number of free blocks for unpriviliged users
        # f_files – number of inodes
        # f_ffree – number of free inodes
        # f_favail – number of free inodes for unpriviliged users
        # f_flag – mount flags
        # f_namemax – maximum filename length



#print(machine.rng()) #a 24-bit software generated random number. does not work in Pico
#print(machine.deepsleep())  #Stops the CPU and all peripherals (including networking interfaces, if any). Execution is resumed from the main script, just as with a reset
#print(machine.idle())

# working with Pins and GPIO
import utime
from machine import Pin
p_out = Pin(25, mode=Pin.OUT)
for i in range(10):
    print(i*i)
    p_out.toggle()
    utime.sleep(1.5)

# I2C Scanner Code
import machine
sda=machine.Pin(8)
scl=machine.Pin(9)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=400000)

print('Scan i2c bus...')
devices = i2c.scan()

if len(devices) == 0:
  print("No i2c device !")
else:
  print('i2c devices found:',len(devices))

  for device in devices:
    print("Decimal address: ",device," | Hexa address: ",hex(device))


import random
from machine import Pin

def main():
    selection= random.randint(2000,2800)
    while selection < 2990:
        selection = random.randint(10,3000)
        print(selection)
    print("Game Over")



if __name__ == "__main__" :
    led = Pin(25,Pin.OUT)
    led.high()
    main()
    led.low()


from machine import Pin
import utime

# measuring_time
def main_measuring_time():
    led = Pin(25,Pin.OUT)
    print(utime.localtime())
    for i in range(10):
        #print(i)
        led.high()
        utime.sleep_ms(i*40)
        led.low()
        utime.sleep_ms(i*40)


if __name__ == "__main__" :
    #led.high()
    #utime.sleep(1) #Sleep for the given number of seconds
    start_ms = utime.ticks_ms()#increasing millisecond counter with an arbitrary reference point
    start_us = utime.ticks_us()
    print("Starting point {}\t\t {}".format(start_ms, start_us))
    main_measuring_time()
    utime.sleep(1)
    finish_ms = utime.ticks_ms()#increasing millisecond counter with an arbitrary reference point
    finish_us = utime.ticks_us()
    print("Interval length: {} ms \t\t {} us".format(finish_ms - start_ms, finish_us- start_us))
