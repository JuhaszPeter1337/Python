class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self) -> int:
        """Define behavior of len() function"""
        return self.size
    
    def __getitem__(self, index: int) -> "Node":
        """Enable indexing: obj[index]"""
        if index >= self.size or index < 0:
            raise IndexError("Index out of range!")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value
    
    def __setitem__(self, index: int, value: int):
        """Enable item assignment: obj[index] = value"""
        if index >= self.size or index < 0:
            raise IndexError("Index out of range!")
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def __delitem__(self, index: int):
        """Delete an item: del obj[index]"""
        if index >= self.size or index < 0:
            raise IndexError("Index out of range!")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def __contains__(self, value: int) -> bool:
        """Define behavior for 'in' keyword"""
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False
    
    def append(self, value):
        """Add a new node to the end of the list"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            for _ in range(self.size - 1):
                current = current.next
            """ OR
            while current.next:
                current = current.next
            """
            current.next = new_node
        self.size += 1\
        
    def __str__(self):
        """User-friendly string representation"""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)
        
if __name__ == "__main__":
    my_list = LinkedList()
    my_list.append(5)
    my_list.append(3)
    my_list.append(10)

    print(f"Length: {len(my_list)}")
    print(f"Item 0: {my_list[0]}")
    print(f"Item 1: {my_list[1]}")
    print(f"Item 2: {my_list[2]}")
    print(my_list)

    del my_list[2]
    my_list[1] = 8
    print(my_list)
    
    print(10 in my_list)