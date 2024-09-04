from modules.Monster_Fight import monster_fight

def command_parsing(command):
    """
    Parse player command 

    Args:
        command (string): The command entered by player in the input (key='-IN-')

    Returns:
        str: The direction or error information (None)
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
        
def fighting():
    pass


if __name__ == "__main__":
    pass