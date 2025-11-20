# utils

from labyrinth_game.player_actions import get_input

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


def solve_puzzle(game_state):
    """Позволяет игроку решать загадку в текущей комнате."""
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

    puzzle = room_data.get('puzzle')

    # Нет загадки → выводим сообщение и выходим
    if not puzzle:
        print("Загадок здесь нет.")
        return

    # Печатаем текст загадки
    print("\nЗагадка:")
    print(puzzle['question'])

    # Получаем ответ игрока
    answer = get_input("Ваш ответ: ").strip().lower()

    # Проверка
    if answer == puzzle['answer'].lower():
        print("Верно! Вы решили загадку.")

        # Выдаём награду, если есть
        reward = puzzle.get('reward')
        if reward:
            print(f"Вы получили: {reward}")
            game_state['player_inventory'].append(reward)

            # Если загадка связана с открытием сундука — победа
            if reward == "treasure_unlock":
                attempt_open_treasure(game_state)
                return

        # Удаляем загадку, чтобы нельзя было решать повторно
        room_data['puzzle'] = None

    else:
        print("Неверно. Попробуйте снова.")


def attempt_open_treasure(game_state):
    """
    Логика открытия сокровищницы и победы.
    Игрок может победить двумя способами:
    - Использовать treasure_key на сундук
    - Решить загадку, открывающую сундук (reward = 'treasure_unlock')
    """
    current_room = game_state['current_room']
    room_data = ROOMS[current_room]

    # Проверяем наличие сундука
    if "treasure_chest" not in room_data.get("items", []):
        print("Здесь нет сундука.")
        return

    # Сценарий: у игрока есть ключ
    if "treasure_key" in game_state["player_inventory"]:
        print("Вы применяете ключ, и замок щёлкает. Сундук открыт!")
        room_data["items"].remove("treasure_chest")
        print("В сундуке сокровище! 🎉 Вы победили!")
        game_state["game_over"] = True
        return

    # Сценарий: сундук можно открыть решением загадки
    if "treasure_unlock" in game_state["player_inventory"]:
        print("Механизм внутри сундука щёлкает — загадка открыла его!")
        room_data["items"].remove("treasure_chest")

        print("В сундуке сокровище! 🎉 Вы победили!")
        game_state["game_over"] = True
        return

    # Сценарий: нет ключа и награды
    print("У вас нет ключа, чтобы открыть сундук.")
    choice = get_input("Хотите попробовать ввести код? (да/нет): ").strip().lower()
    if choice in ("да", "yes", "y"):
        puzzle = room_data.get("puzzle")
        if puzzle:
            code = get_input("Введите код: ").strip().lower()
            if code == puzzle["answer"].lower():
                print("Код верный! Замок открывается.")
                room_data["items"].remove("treasure_chest")
                print("В сундуке сокровище! 🎉 Вы победили!")
                game_state["game_over"] = True
            else:
                print("Код неверный. Замок остаётся закрытым.")
        else:
            print("В сундуке нет загадки для взлома.")
    else:
        print("Вы отступаете от сундука.")


def show_help():
    """Выводит список доступных команд для игрока."""
    print("\nДоступные команды:")
    print("  go <direction>  - перейти в направлении (north/south/east/west)")
    print("  look            - осмотреть текущую комнату")
    print("  take <item>     - поднять предмет")
    print("  use <item>      - использовать предмет из инвентаря")
    print("  inventory       - показать инвентарь")
    print("  solve           - попытаться решить загадку в комнате")
    print("  quit            - выйти из игры")
    print("  help            - показать это сообщение")