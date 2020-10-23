import wpilib

class OI:
    def __init__(self):
        self.joystick = wpilib.Joystick(1) #Make a joystick on port one
        self.inSpeed = 0 #X value of the joystick is speed
        self.inTurn = 0 #Y value of the joystick is turn rate

    def execute(self):
        '''Runs every control loop'''
        self.inSpeed = self.joystick.getX()
        self.inTurn = self.joystick.getY()