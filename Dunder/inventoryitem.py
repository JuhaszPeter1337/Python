from typing import Union

class InventoryItem():
    """A class to demonstrate operator overloading for inventory management."""
    def __init__(self, name: str, quantity: int):
        self.name = name
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"InventoryItem(name='{self.name}', quantity={self.quantity})"
    
    def __add__(self, other: "InventoryItem") -> "InventoryItem":
        if isinstance(other, InventoryItem) and other.name == self.name:
            return InventoryItem(self.name, self.quantity + other.quantity)
        else:
            raise TypeError("Invalid type of object!")
        
    def __sub__(self, other: "InventoryItem") -> "InventoryItem":
        if isinstance(other, InventoryItem) and other.name == self.name:
            if self.quantity >= other.quantity:
                return InventoryItem(self.name, self.quantity - other.quantity)
            raise ValueError("Cannot subtract more than the available quantity.")
        raise TypeError("Invalid type of object!")
    
    # factor: Union[int, float] or factor: int | float
    def __mul__(self, factor: Union[int, float]) -> "InventoryItem":
        if isinstance(factor, (int, float)):
            return InventoryItem(self.name, self.quantity * factor)
        raise TypeError("Invalid type of object!")
    
    # factor: Union[int, float] or factor: int | float
    def __truediv__(self, factor: Union[int, float]) -> "InventoryItem":
        if isinstance(factor, (int, float)) and factor != 0:
            return InventoryItem(self.name, self.quantity / factor)
        raise TypeError("Invalid type of object!")
    
    """Comparison operators"""
    def __eq__(self, other: "InventoryItem") -> bool:
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.quantity == other.quantity
        return False
    
    def __lt__(self, other: "InventoryItem") -> bool:
        if isinstance(other, InventoryItem):
            return self.quantity < other.quantity
        raise TypeError("Invalid type of object!")
    
    def __gt__(self, other: "InventoryItem") -> bool:
        if isinstance(other, InventoryItem):
            return self.quantity > other.quantity
        raise TypeError("Invalid type of object!")
    
    def __le__(self, other: "InventoryItem") -> bool:
        if isinstance(other, InventoryItem):
            return self.quantity <= other.quantity
        raise TypeError("Invalid type of object!")

    def __ge__(self, other: "InventoryItem") -> bool:
        if isinstance(other, InventoryItem):
            return self.quantity >= other.quantity
        raise TypeError("Invalid type of object!")

if __name__ == "__main__":
    # Define inv, inv2 objects
    inv = InventoryItem("Banana", 5)
    inv2 = InventoryItem("Banana", 10)
    
    # Use __repr__() function
    print(repr(inv))

    # Add items if possible
    try:
        inv = inv + inv2
        print(repr(inv))
    except TypeError as e:
        print(e)

    # Define inv3, inv4 objects
    inv3 = InventoryItem("Banana", 4)
    inv4 = InventoryItem("Banana", 5)
    
    # Subtract items if possible
    try:
        inv3 = inv3 - inv4
    except ValueError as e:
        print(e)
    
    # Multiple if possible
    try:
        inv2 = inv2 * 5
        print(inv2)
    except TypeError as e:
        print(e)
    
    # Divide if possible
    try:
        inv2 = inv2 / 5
        print(inv2)
    except TypeError as e:
        print(e)

    # Check inv < inv2
    print(repr(inv2), repr(inv))
    print(inv < inv2)
