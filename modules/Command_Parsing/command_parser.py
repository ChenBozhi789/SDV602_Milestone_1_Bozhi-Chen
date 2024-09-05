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
    if command.startswith('go '):
        direction = command[3:] # Get the copy of direction, start from index 0
    elif command.startswith('walk to '): # index 8
        direction = command[8:] # Get the copy of direction, start from index 8
    elif command.startswith('move to '): # index 8
        direction = command[8:] # Get the copy of direction, start from index 8
    elif command.startswith(''): # Check if command is a direction
        direction = command[0:] # Get the copy of direction, start from index 3
    else:
        return None
    
    if direction in directions:
        return direction
    else:
        return None
        
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
    if command in action:
        return command
    else:
        return None
    
def status_parsing(command):
    """
    Parse player status command 

    Args:
        command (string): The command entered by player in the input (key='-IN-')

    Returns:
        str: status
    """
    command = command.lower().strip()
    if command == 'status':
        return command
    else:
        return None
    
if __name__ == "__main__":
    pass