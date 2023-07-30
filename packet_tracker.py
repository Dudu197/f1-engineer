from copy import deepcopy

class PacketTracker:
    tracking = {}
    old_tracked_data = None
    tracked_data = {}
    changed = []

    def __init__(self, track):
        self.tracking = track
        for key, values in self.tracking.items():
            self.tracked_data[key] = {v: None for v in values}
        self.old_tracked_data = deepcopy(self.tracked_data)

    def track(self, data):
        player_car_index = data["header"]["player_car_index"]
        for key, values in self.tracking.items():
            if key in data.keys():
                item_data = data[key][player_car_index]
                for v in values:
                    value = item_data[v]
                    if type(value) == list:
                        value = tuple(value)
                    self.tracked_data[key][v] = value
                    if self.old_tracked_data[key][v] is None:
                        self.old_tracked_data[key][v] = value

    def get_changed_data(self):
        changed = []
        for key in self.tracked_data.keys():
            old_values = set(self.old_tracked_data[key].items())
            new_values = set(self.tracked_data[key].items())
            changed_values = new_values - old_values
            changed += [f"{i[0]} changed from {self.old_tracked_data[key][i[0]]} to {i[1]}" for i in changed_values]
        self.old_tracked_data = deepcopy(self.tracked_data)
        return "\n".join(changed) if len(changed) > 0 else None

