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