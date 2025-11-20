#!/usr/bin/env python3

# Подключаем собственные модули проекта
from .constants import ROOMS

# Состояние игры
game_state = {
    'player_inventory': [],  # Инвентарь игрока
    'current_room': 'entrance',  # Текущая комната
    'game_over': False,  # Флаг окончания игры
    'steps_taken': 0  # Количество сделанных шагов
}


def main():
    # Пример: вывод всех комнат с предметами и загадками
    print("Список комнат в лабиринте:")
    for room_name, room_data in ROOMS.items():
        print(
            f"- {room_name}: items = {room_data['items']}, "
            f"puzzle = {room_data['puzzle']}"
        )

if __name__ == "__main__":
    main()