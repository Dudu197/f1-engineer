from f1_22_telemetry.listener import TelemetryListener
from src.tracker import Tracker
from src.trackers import *
from packet_tracker import PacketTracker
import time


class EngineerEngine:
    listener: TelemetryListener
    trackers: list

    def __init__(self):
        self.listener = TelemetryListener(port=20777, host='localhost')
        self.trackers = []
        for cls in Tracker.__subclasses__():
            tracker = cls()
            print("Loading " + tracker.name)
            tracker.race_start()
            self.trackers.append(tracker)

    def start(self):
        while True:
            packet = self.listener.get().to_dict()
            for tracker in self.trackers:
                player_car_index = packet["header"]["player_car_index"]
                tracker.track(packet, player_car_index)
            # print()
            # print(packet)
