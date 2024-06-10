

# class Stack:

#     def __init__(self) -> None:

#         self.items = []

#     def push(self, item):

#         self.items.append(item)

#     def is_empty(self):

#         return len(self.items) == 0

#     def pop(self):

#         if self.is_empty():
#             raise IndexError
#         else:
#             return self.items.pop()

#     def peek(self):

#         if self.is_empty():
#             raise IndexError
#         else:
#             print(self.items[-1])

#     def size(self):

#         if self.is_empty():
#             raise IndexError
#         else:
#             print(len(self.items))

# if __name__ == "__main__":

#     s1 = Stack()
#     s1.push(10)
#     s1.push(20)
#     s1.push(30)
#     s1.size()
#     s1.peek()
#     print(s1.is_empty())
#     s1.pop()
#     s1.size()


