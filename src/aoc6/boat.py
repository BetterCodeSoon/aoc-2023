class Boat:

    def __init__(self, max_race_duration: int):
        if max_race_duration is None:
            raise ValueError("The maximum time for a race cannot be None!\n")
        self.max_race_duration: int = max_race_duration
        self.speed: int = 0  # unit of millimeters per millisecond
        self.distance_traveled = 0  # unit is millimeters

    def hold_button(self, time_button_pressed):
        if time_button_pressed >= self.max_race_duration:
            raise ValueError(f"The button has been held down for too long. The Boat will move 0mm\n"
                             f"Race max duration: {self.max_race_duration}ms vs button pressed: {time_button_pressed}ms\n")

        self.speed = time_button_pressed
        self.distance_traveled = self._calc_distance(time_button_pressed, self.max_race_duration)

    @staticmethod
    def _calc_distance(time_button_pressed: int, max_race_duration: int):
        time_left = max_race_duration - time_button_pressed
        return time_button_pressed * time_left
