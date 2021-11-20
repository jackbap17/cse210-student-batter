from game.point import Point

class Actor:
    def __init__(self):
        self._description = ""
        self._text = ""
        self._position = Point(0,0)
        self._velocity = Point(0,0)

    def get_text(self):
        return self._text

    def get_position(self):
        return self._position 

    def get_velocity(self):
        return self._velocity

    def set_text(self, text):
        self._text = text    

    def set_position(self, position):
        self._position = position

    def set_velocity(self, velocity):
        self._velocity = velocity
        

   