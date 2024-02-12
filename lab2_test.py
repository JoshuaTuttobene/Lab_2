import encoder_reader as ER
import pyb
import micropython
import motor_driver as MD

if __name__ == "__main__":
     
    # Motor driver test
    encoder_pin = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP)
    in1pin = pyb.Pin.cpu.B4
    in2pin = pyb.Pin.cpu.B5
    tim3 = pyb.Timer(3, freq=20000)
    motor = MD.MotorDriver(encoder_pin, in1pin, in2pin, tim3)
    motor.enable()
    user = input()
    motor.set_duty_cycle(user)
    
    # Encoder test
    pin_A = pyb.Pin.cpu.C6
    pin_B = pyb.Pin.cpu.C7
    tim8 = pyb.Timer(8, prescaler = 0, period = 2**16-1)
    encoder = ER.Encoder(pin_A, pin_B, tim8)
    
    encoder.zero()
    previous_reading = 0
    while True:
        current_reading = encoder.read()
        print(current_reading)
        
        
