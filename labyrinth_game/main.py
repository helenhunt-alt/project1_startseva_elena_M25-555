#!/usr/bin/env python3

# Подключаем собственные модули проекта
from .player_actions import get_input, move_player, show_inventory, take_item, use_item
from .utils import describe_current_room


def process_command(game_state, command):
    """Обрабатывает введённую пользователем команду."""

    if not command:
        return

    parts = command.lower().split()
    action = parts[0]
    arg = parts[1] if len(parts) > 1 else None

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
                take_item(game_state, arg)
            else:
                print("Что взять? Например: take torch")

        case "use":
            if arg:
                use_item(game_state, arg)
            else:
                print("Что использовать? Например: use torch")

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