import machine
print(machine.freq())  #125000000
print(machine.freq() * 1.0/ (1000*1000))  #125.0
help(machine)
print(machine.__name__)
print(machine.unique_id()) # b"\xe6`\x10\xb6C,0'" #Returns a byte string with a unique identifier of a board/SoC

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
