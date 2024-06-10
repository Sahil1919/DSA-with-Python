


class Stack(list):

    def push(self, item):

        self.append(item)

    def is_empty(self):

        return len(self) == 0

    def pop(self):

        if self.is_empty():
            raise IndexError
        else:
            ''' POP is method is override, 
             so in this case will use super() 
             for calling the Parent class method'''
            return super().pop() 

    def peek(self):

        if self.is_empty():
            raise IndexError
        else:
            print(self[-1])

    def size(self):

        if self.is_empty():
            raise IndexError
        else:
            print(len(self))

    # TO restrict some parent class method for accessing
    def insert(self, *args, **kwargs):
        raise AttributeError("Method 'insert' is not allowed for Stack instances.")

if __name__ == "__main__":

    s1 = Stack()
    s1.push(10)
    s1.push(20)
    s1.push(30)
    s1.size()
    s1.peek()
    print(s1.is_empty())
    s1.pop()
    s1.size()
    s1.insert(10,20)


