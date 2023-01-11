from djitellopy import Tello

class TelloKeyboardController:
    def __init__(self, tello: Tello):
        self.tello = tello
        self.in_flight=False

    def control(self, key):

        if key == ord('w'):
            self.tello.move_forward(30)
        elif key == ord('s'):
            self.tello.move_back(30)
        elif key == ord('a'):
            self.tello.move_left(30)
        elif key == ord('d'):
            self.tello.move_right(30)
        elif key == ord('e'):
            self.tello.rotate_clockwise(30)
        elif key == ord('q'):
            self.tello.rotate_counter_clockwise(30)
        elif key == ord('r'):
            self.tello.move_up(30)
        elif key == ord('f'):
            self.tello.move_down(30)
        elif key == 0:
            self.tello.flip_forward()
        elif key ==1:
            self.tello.flip_back()
        elif key == 2:
            self.tello.flip_left()
        elif key == 3:
            self.tello.flip_right()
        elif key == ord('u'):
            self.tello.emergency()
       


