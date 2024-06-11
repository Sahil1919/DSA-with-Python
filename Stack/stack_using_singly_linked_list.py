
class Node:

    def __init__(self,item=None,next=None) -> None:
        
        self.item = item
        self.next = next

class Stack:

    def __init__(self) -> None:
        
        self.start = None
        self.item_count = 0

    def is_empty(self):

        return self.start == None
    
    def push(self,item):

        node = Node(item,self.start)
        self.start = node
        self.item_count += 1

    def pop(self):

        if self.is_empty():

            raise IndexError("Stack is EMPTY")
        
        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data
        
    def peek(self):

        if self.is_empty():

            raise IndexError("Stack is EMPTY")
        
        else:
            return self.start.item

    def size(self):

        return self.item_count
    

if __name__ == "__main__":

    s1 = Stack()
    s1.push(10)
    s1.push(20)
    s1.push(30)
    print(s1.size())
    print(s1.peek())
    print(s1.is_empty())
    print(s1.pop())
    print(s1.peek())
    print(s1.size())