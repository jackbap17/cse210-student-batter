from game.action import Action

class DrawActorsAction(Action):

    def __init__(self, output_service):
        self._output_service = output_service

    def execute(self, cast):
        self._output_service.clear_screen()
        for group in cast.values():
            self._output_service.draw_actors(group)
        self._output_service.flush_buffer()    