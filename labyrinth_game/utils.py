# utils

from .constants import ROOMS


def describe_current_room(game_state):
    """Выводит описание текущей комнаты"""
    current_room_name = game_state['current_room']
    room_data = ROOMS[current_room_name]

    # Название комнаты в верхнем регистре
    print(f"\n== {current_room_name.upper()} ==")

    # Описание комнаты
    print(room_data['description'])

    # Видимые предметы
    if room_data['items']:
        print("Заметные предметы:", ", ".join(room_data['items']))

    # Доступные выходы
    exits = ", ".join(room_data['exits'].keys())
    print("Выходы:", exits)

    # Сообщение о загадке
    if room_data['puzzle']:
        print("Кажется, здесь есть загадка (используйте команду solve).")