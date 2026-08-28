from pid import PID

class GimbalController:

    def __init__(self):

        self.pan = PID(0.08,0.001,0.02)
        self.tilt = PID(0.08,0.001,0.02)

    def track(self,target,frame_width,frame_height):

        if target is None:
            return

        x,y,w,h = target.tlwh

        cx = x + w/2
        cy = y + h/2

        error_x = frame_width/2 - cx
        error_y = frame_height/2 - cy

        yaw = self.pan.update(error_x)
        pitch = self.tilt.update(error_y)

        print(yaw,pitch)

        # Send commands to Skydroid