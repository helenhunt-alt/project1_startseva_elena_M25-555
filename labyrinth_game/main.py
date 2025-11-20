#!/usr/bin/env python3

# Подключаем собственные модули проекта
from labyrinth_game.constants import ROOMS
from labyrinth_game.player_actions import get_input, show_inventory
from labyrinth_game.utils import describe_current_room

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
        if command.lower() in ['quit', 'exit']:
            print("Вы вышли из игры.")
            break

        # Заглушка: пока обрабатываем только команды 'inventory' и 'look'
        if command.lower() in ['inventory', 'inv']:
            show_inventory(game_state)
        elif command.lower() in ['look', 'describe']:
            describe_current_room(game_state)
        else:
            print("Команда пока не реализована.")

if __name__ == "__main__":
    main()