import wpilib

from drivetrain import Drivetrain


class Robot(wpilib.TimedRobot):
    def __init__(self):
        super().__init__()
        self.drivetrain = Drivetrain()

    def robotInit(self):
        pass

    def robotPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        self.drivetrain.set(1, 1)

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass


if __name__ == "__main__":
    wpilib.run(Robot)
