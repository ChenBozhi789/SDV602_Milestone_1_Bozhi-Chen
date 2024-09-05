from modules.Monster_Fight import monster_fight
from modules.Player_Inventory import inventory

def movement_parsing(command):
    """
    Parse player command 

    Args:
        command (string): The command entered by player in the input (key='-IN-')

    Returns:
        str: direction or None
    """
    directions = ['north', 'south', 'west', 'east'] # Use list to store all directions
    command = command.lower().strip() # Convert to lower and remove all whitespace
    direction = next((command[(len(prefix)+1):] for prefix in ['go', 'move to', 'walk to'] if command.startswith(prefix)), command)
    return direction if direction in directions else None
        
def fighting_parsing(command):
    """
    Parse player fighting command 

    Args:
        command (string): The command entered by player in the input (key='-IN-')

    Returns:
        str: action
    """
    action = ['attack', 'heal', 'run', 'pick up', 'inventory']
    command = command.lower().strip()
    return command if command in action else None
    
def status_parsing(command):
    """
    Parse player status command 

    Args:
        command (string): The command entered by player in the input (key='-IN-')

    Returns:
        str: status
    """
    command = command.lower().strip()
    return command if command == 'status' else None
    
if __name__ == "__main__":
    pass