from typing import Any
from src.tracker import Tracker


class PaceTracker(Tracker):
    name = "Pace Tracker"
    events = ["lap_data"]

    current_lap: int
    best_time: float
    last_time: float

    def race_start(self):
        self.current_lap = 0
        self.best_time = -1.0
        self.last_time = -1.0

    def tick(self, event: str, data: Any, player_car_index: int):
        player_lap = data[player_car_index]
        current_lap = player_lap["current_lap_num"]
        if self.current_lap < current_lap:
            self.current_lap = current_lap
            last_lap_time = player_lap["last_lap_time_in_ms"] / 1000.0
            current_lap_time = player_lap["current_lap_time_in_ms"] / 1000.0
            self.last_time = last_lap_time
            if last_lap_time < self.best_time or self.best_time == -1.0:
                self.best_time = last_lap_time

            best_lap_delta = self.best_time - last_lap_time

            self.speak("Delta última volta: " + str(best_lap_delta))



            print("="*8)
            print("Delta última volta: " + str(best_lap_delta))
            print(f"""
    Current Lap: {current_lap}
    Last Lap Time: {last_lap_time}
    Current Lap Time: {current_lap_time}
            """)
