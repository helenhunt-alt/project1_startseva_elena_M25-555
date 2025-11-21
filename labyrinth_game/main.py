#!/usr/bin/env python3

# Подключаем собственные модули проекта
from .constants import COMMANDS, ROOMS
from .player_actions import move_player, show_inventory, take_item, use_item
from .utils import (
    attempt_open_treasure,
    describe_current_room,
    get_input,
    show_help,
    solve_puzzle,
)


def process_command(game_state, command):
    """Обрабатывает введённую пользователем команду."""

    if not command:
        return

    parts = command.lower().split()
    action = parts[0]
    arg = parts[1] if len(parts) > 1 else None

    # Движение без go (north, south...)
    directions = {"north", "south", "east", "west", "up", "down"}
    if action in directions:
        move_player(game_state, action)
        return

    match action:
        case "look" | "describe":
            describe_current_room(game_state)

        case "inventory" | "inv":
            show_inventory(game_state)

        case "go" | "move":
            if arg:
                move_player(game_state, arg)
            else:
                print("Куда идти? Например: go north")

        case "take" | "get":
            if arg:
                if arg == "treasure_chest":
                    print("Вы не можете поднять сундук, он слишком тяжелый.")
                else:
                    take_item(game_state, arg)
            else:
                print("Что взять? Например: take torch")

        case "use":
            if arg:
                use_item(game_state, arg)
            else:
                print("Что использовать? Например: use torch")

        case "solve":
            current_room = game_state['current_room']
            # В комнате с treasure_chest сначала проверяем возможность победы
            if "treasure_chest" in ROOMS[current_room].get("items", []):
                attempt_open_treasure(game_state)
            else:
                solve_puzzle(game_state)

        case "help":
            show_help(COMMANDS)

        case "quit" | "exit":
            print("Вы вышли из игры.")
            game_state["game_over"] = True

        case _:
            print("Неизвестная команда.")


def main():
    # Инициализация состояния игры
    game_state = {
        'player_inventory': [],
        'current_room': 'entrance',
        'game_over': False,
        'steps_taken': 0
    }

    # Приветствие
    print("Добро пожаловать в Лабиринт сокровищ!")

    # Описание стартовой комнаты
    describe_current_room(game_state)

    # Основной игровой цикл
    while not game_state['game_over']:
        command = get_input("> ")
        process_command(game_state, command)

if __name__ == "__main__":
    main()