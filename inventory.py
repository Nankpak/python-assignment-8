"""
TASK: Create an Inventory class.

Requirements:
1. Store items in a dictionary (item_name → quantity).
2. Provide a method to add items (with quantity).
3. Provide a method to remove items (only if available).
4. Provide a method to update stock levels.
5. Provide a method to display all inventory items.

Example Usage:
    treasure_store = Inventory()
    favour_store = Inventory()

    treasure_store.add_item("Apples", 50)
    treasure_store.add_item("Bananas", 30)
    treasure_store.remove_item("Apples", 10)
    print(treasure_store.show_inventory())  # {"Apples": 40, "Bananas": 30}

    favour_store.add_item("Milk", 50)
    favour_store.add_item("Garri", 30)
    favour_store.remove_item("Milk", 40)
    print(treasure_store.show_inventory())  # {"Milk": 10, "Garri": 30}
"""
class Inventory:
    def __init__(self,treasure_store):
        self.treasure_store = {'milk':10}
    def add_item(self,key,value):
        
        return self.treasure_store.update({key:value})
    def remove(self,remove):
        del self.treasure_store[remove]
        print(self.treasure_store)
invent = Inventory('milk')
print(invent.add_item('milk',200))
print(invent.add_item('popcorn',3))
print(invent.add_item('popo',200))

invent.remove('milk')

        
