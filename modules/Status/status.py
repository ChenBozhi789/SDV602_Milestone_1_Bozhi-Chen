from modules.Monster_Fight import monster_fight
from modules.Player_Inventory import inventory

def check_status():
    """
    Check the current status of the player

    Args:
        command (string): The command entered by player in the input (key='-IN-')

    Returns:
        str: status
    """
    inventory_list = ", ".join(inventory.inventory_check())
    player_health = monster_fight.player['health']
    player_attack = monster_fight.player['attack']

    current_status = {
        'health': player_health,
        'attack': player_attack,
        'inventory': inventory_list
    }

    return current_status

if __name__ == "__main__":
    pass