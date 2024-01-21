import itertools

from tqdm import tqdm

from common.constants import AVAILABLE_ROOMS, POSITIONS, OBJ_COLORS
from common.house import House
from common.objects import get_obj_style, DecorumObject
from common.rooms import Room

init_bedroom1 = Room("bedroom1", "red")
init_bedroom2 = Room("bedroom1", "green")
init_livingroom = Room("livingroom", "green")
init_kitchen = Room("kitchen", "blue")


def create_and_place_objects(room, color_combination):
    for pos, color in zip(['left', 'middle', 'right'], color_combination):
        obj_type = room.get_type_from_pos(pos)
        obj_style = get_obj_style(color, obj_type)
        if obj_style is not None:
            room.place_object(DecorumObject(obj_type, color, obj_style))

def iter_modifications():
    wall_colors = OBJ_COLORS
    wall_combinations = itertools.product(wall_colors, repeat=len(AVAILABLE_ROOMS))
    object_combinations = itertools.product(OBJ_COLORS + [None], repeat=len(POSITIONS))
    room_combinations = itertools.product(object_combinations, repeat=len(AVAILABLE_ROOMS))

    for wall_combination in wall_combinations:
        for room_combination in tqdm(room_combinations):
            house = House(
                Room('bedroom1', wall_combination[0]),
                Room('bedroom2', wall_combination[1]),
                Room('livingroom', wall_combination[2]),
                Room('kitchen', wall_combination[3])
            )

            for room, color_combination in zip(house.all_rooms, room_combination):
                create_and_place_objects(room, color_combination)

            house.check_example_condition()


if __name__ == '__main__':
    iter_modifications()
