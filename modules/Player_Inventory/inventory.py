inventory = []

def add_item(item):
    """
    Add item to the inventory

    Args:
        item (str): The item to be added to the inventory
    """
    inventory.append(item)
    print(inventory)
    return f"You have picked up {item}"

def inventory_check():
    return inventory

if __name__ == "__main__":
    pass