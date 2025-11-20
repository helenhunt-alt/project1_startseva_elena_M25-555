# player_actions

from .constants import ROOMS
from .utils import describe_current_room


def show_inventory(game_state):
    """Выводит содержимое инвентаря игрока"""
    inventory = game_state['player_inventory']
    if inventory:
        print("Инвентарь:", ", ".join(inventory))
    else:
        print("Инвентарь пуст.")


def get_input(prompt="> "):
    """Считывает ввод пользователя с обработкой прерываний"""
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print("\nВыход из игры.")
        return "quit"


def move_player(game_state, direction):
    current_room = game_state["current_room"]
    room_data = ROOMS[current_room]

    if direction in room_data["exits"]:
        new_room = room_data["exits"][direction]
        game_state["current_room"] = new_room
        game_state["steps_taken"] += 1

        print(f"\nВы переместились в комнату: {new_room}\n")
        describe_current_room(game_state)
    else:
        print("Нельзя пойти в этом направлении.")


def take_item(game_state, item_name):
    """Поднять предмет из комнаты и положить в инвентарь"""
    current_room = game_state["current_room"]
    room_data = ROOMS[current_room]

    if item_name in room_data["items"]:
        game_state["player_inventory"].append(item_name)
        room_data["items"].remove(item_name)
        print(f"Вы подняли: {item_name}")
    else:
        print("Такого предмета здесь нет.")


def use_item(game_state, item_name):
    """Использовать предмет из инвентаря"""

    inventory = game_state['player_inventory']

    if item_name not in inventory:
        print("У вас нет такого предмета.")
        return

    # Логика использования предметов
    match item_name:
        case "torch":
            print("Вы подняли факел выше — стало светлее.")

        case "sword":
            print("Вы крепче сжали меч. Чувствуете себя увереннее.")

        case "bronze_box":
            print("Вы открыли бронзовую шкатулку...")
            if "rusty_key" not in inventory:
                inventory.append("rusty_key")
                print("Внутри лежал ржавый ключ! Он добавлен в ваш инвентарь.")
            else:
                print("Но внутри пусто.")

        case _:
            print("Вы не знаете, как использовать этот предмет.")