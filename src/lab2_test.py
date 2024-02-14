"""!
@file lab2_test.py

This file contains code to test the encoder.
This includes code needed to zero and run the encoder and print the current reading.
Additionally code to run a motor using our motor drivers is included to ease in testing
of overflow and underflow.

@author Aaron Escamilla, Karen Morales De Leon, Joshua Tuttobene
@date   02/15/2024 Original program
@copyright (c) 2023 by Spluttflob and released under the GNU Public Licenes V3
"""
import encoder_reader as ER
import pyb
import micropython
import motor_driver as MD
import utime

if __name__ == "__main__":
     
    # Motor driver test
    encoder_pin = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    in1pin = pyb.Pin.cpu.B4
    in2pin = pyb.Pin.cpu.B5
    tim3 = pyb.Timer(3, freq=20000)
    motor = MD.MotorDriver(encoder_pin, in1pin, in2pin, tim3)
    motor.enable()
    user = input("Enter a motor duty cycle from -100 to 100:")
    motor.set_duty_cycle(user)
    
    # Encoder test
    pin_A = pyb.Pin.cpu.C6
    pin_B = pyb.Pin.cpu.C7
    tim8 = pyb.Timer(8, prescaler = 0, period = 2**16-1)
    encoder = ER.Encoder(pin_A, pin_B, tim8)
    
    encoder.zero()
    p=1000
    while p>0:        # run for an arbitrary number of cycles
        print(encoder.read())
        p-=1
    
    encoder.zero()  # zero encoder
    print(encoder.read()) # print encoder reading immeadiatley after zeroing to show success 
    while True:        # while loop to show sucessful overflow and underflow
        print(encoder.read())
        #utime.sleep(.5)