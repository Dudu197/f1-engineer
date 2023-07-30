from src.engieneer_engine import EngineerEngine


# tracker = PacketTracker({
#     "car_damage_data": [
#         # "tyres_damage",
#         "front_left_wing_damage",
#         "front_right_wing_damage",
#         "rear_wing_damage",
#         "floor_damage",
#         "diffuser_damage",
#         "sidepod_damage",
#     ],
#     "car_telemetry_data": [
#         "brakes_temperature",
#         "tyres_surface_temperature",
#         "tyres_inner_temperature",
#         "engine_temperature",
#         "tyres_pressure",
#         "surface_type",
#     ]
# })

engineer = EngineerEngine()

engineer.start()
