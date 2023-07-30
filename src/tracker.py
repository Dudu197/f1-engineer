from abc import ABC, abstractmethod
from typing import Any
import pyttsx3


class Tracker(ABC):
    name: str = None
    events = []
    __speech = pyttsx3.init()

    @abstractmethod
    def tick(self, event: str, data: Any, player_car_index: int):
        pass

    @abstractmethod
    def race_start(self):
        pass

    def track(self, data: dict, player_car_index: int):
        for key in data.keys():
            if key in self.events:
                self.tick(key, data[key], player_car_index)

    def speak(self, text):
        self.__speech.say(text)
        self.__speech.runAndWait()
