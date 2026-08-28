class PID:

    def __init__(self, kp, ki, kd):

        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.previous = 0
        self.integral = 0

    def update(self, error):

        self.integral += error

        derivative = error - self.previous

        self.previous = error

        return (
            self.kp * error +
            self.ki * self.integral +
            self.kd * derivative
        )