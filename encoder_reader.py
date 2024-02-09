import pyb

class Encoder:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, pin_A, pin_B, timer):
        """! 
        Initializes the encoder reader by enabling the pins and the timer
        @param en_pin (There will be several parameters)
        """
        # Set up for each parameter. This will be called in other program
        self.pin_A = pin_A
        self.pin_B = pin_B
        self.timer = timer
        self.ch1 = timer.channel(1, pyb.Timer.ENC_AB, pin=pin_A)
        self.ch2 = timer.channel(2, pyb.Timer.ENC_AB, pin=pin_B)
        print ("Initializing")

    def read (self, previous_reading):
        """!
        This method reads the current value of the encoder
        """
        current_reading = self.timer.counter()
        delta = current_reading - previous_reading
        
        if delta >= 2**16//2:
            delta = -2**16
                
        elif delta <= -2**16//2:
            delta = 2**16
        current_reading += delta    
        return current_reading
        
    def zero (self):
        """!
        This method returns a value of zero to the encoder 
        """
        print("Zeroed")
        self.timer.counter(0)
    