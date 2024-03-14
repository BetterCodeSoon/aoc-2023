class Boat:

    @staticmethod
    def calc_distance(time_button_pressed: int, max_race_duration: int):
        time_left = max_race_duration - time_button_pressed
        return time_button_pressed * time_left
