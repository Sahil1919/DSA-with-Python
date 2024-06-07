
class Node:

    def __init__(self, prev=None, item=None, next=None) -> None:

        self.prev = prev
        self.item = item
        self.next = next


class DLL:

    def __init__(self, start=None) -> None:

        self.start = start

    def __iter__(self):
        self.current = self.start
        return self
    
    def __next__(self):

        if not self.current:
            raise StopIteration
        
        item = self.current.item
        self.current = self.current.next
        return item



    def is_empty(self):

        return self.start == None

    def insert_at_start(self, item):

        node = Node(item=item, next=self.start)

        if not self.is_empty():
            self.start.prev = node

        self.start = node

    def insert_at_last(self, item):

        if self.is_empty():
            self.insert_at_start(item)

        else:
            temp = self.start

            while temp.next is not None:
                temp = temp.next

            temp.next = Node(prev=temp, item=item)

    def search(self, item):

        temp = self.start

        while temp is not None:
            if temp.item == item:
                return temp

            temp = temp.next

        return None

    def get_index_of_node(self, item):

        temp = self.start
        index = 1

        while temp is not None:
            if temp.item == item:
                return index
            temp = temp.next
            index += 1

        return -1

    def insert_after(self, insert_after_item, item_to_be_insert):

        node_info = self.search(insert_after_item)

        if node_info:

            node = Node(prev=node_info, item=item_to_be_insert,
                        next=node_info.next)
            node_info.next = node

    def print_list_items(self):

        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()

    def delete_first(self):

        if not self.is_empty():
            self.start = self.start.next
            self.start.prev = None

    def delete_last(self):

        if not self.is_empty():

            if self.start.next is None:
                self.start = None

            else:
                temp = self.start

                while temp.next.next is not None:
                    temp = temp.next

                temp.next = None

    def delete_item(self, item):

        if not self.is_empty():

            if self.start.item == item:
                self.delete_first()

            else:
                temp = self.start
                while temp.next.item != item:
                    temp = temp.next

                temp.next = temp.next.next

if __name__ == '__main__':

    dll = DLL()

    """ Elementary Operation Performance END """
    # dll.insert_at_start(20)
    # dll.insert_at_start(10)
    # dll.insert_at_last(30)
    # dll.insert_at_last(50)
    # # print(dll.search(30))
    # # dll.insert_after(30, 40)
    # # dll.print_list_items()
    # # dll.delete_first()
    # # dll.print_list_items()
    # # dll.delete_last()
    # # dll.print_list_items()
    # # dll.delete_item(30)
    # # dll.print_list_items()

    """ Elementary Operation Performance END """

    """ Iterable Printing using Iterator Implicitly  """
    # for item in dll:
    #     print(item)

    """ Iterable Printing using Iterator Explicitly  """
    # dll_iterator = dll.__iter__()
    # print(dll_iterator.__next__())

    """ Second way """
    # dll_iterator = iter(dll)
    # print(next(dll_iterator))
    # print(next(dll_iterator))
    # print(next(dll_iterator))
    # print(next(dll_iterator))
    # print(next(dll_iterator))
