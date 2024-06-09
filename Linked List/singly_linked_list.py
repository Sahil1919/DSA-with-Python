

class Node:

    def __init__(self, item=None, next=None) -> None:

        self.item = item
        self.next = next


class SLL:

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

    def is_empty(self) -> bool:

        return self.start == None

    def insert_at_start(self, item):

        self.start = Node(item, self.start)

    def insert_at_end(self, item):

        if self.is_empty():
            self.insert_at_start(item)
        else:
            temp = self.start
            while temp.next:
                temp = temp.next

            temp.next = Node(item)

    def search(self, item):

        temp = self.start

        while temp:
            if temp.item == item:
                return temp
            temp = temp.next

        return None

    def get_index_of_node(self, item):

        temp = self.start
        index = 1

        while temp:
            if temp.item == item:
                return index
            temp = temp.next
            index += 1

        return -1

    def insert_after(self, insert_after_item, item_to_be_insert):
        node = self.search(insert_after_item)
        if node:
            node.next = Node(item_to_be_insert, node.next)

    def print_list_items(self):

        temp = self.start
        while temp:
            print(temp.item, end=' ')
            temp = temp.next
        print()

    def delete_first(self):

        if not self.is_empty():
            self.start = self.start.next

    def delete_last(self):

        if not self.is_empty():

            if self.start.next is None:
                self.start = None
            else:
                temp = self.start
                while temp.next.next:
                    temp = temp.next

                temp.next = None

    def delete_item(self, item):

        if not self.is_empty():

            if self.start.item == item:
                self.delete_first()

            else:
                temp = self.start.next
                while temp.next.item != item:
                    temp = temp.next

                temp.next = temp.next.next


if __name__ == "__main__":
    sll = SLL()

    """ Elementary Operation Performance START """
    # sll.insert_at_start(20)
    # sll.insert_at_start(10)
    # sll.insert_at_end(40)
    # sll.insert_at_end(50)
    # sll.insert_at_end(60)
    # print(sll.search(30))
    # print(sll.get_index_of_node(30))
    # sll.insert_after(20, 30)
    # sll.print_list_items()
    # sll.delete_first()
    # print()
    # sll.print_list_items()
    # print()
    # sll.delete_last()
    # sll.print_list_items()
    # print("\n")
    # sll.delete_item(40)
    # print()
    # sll.print_list_items()
    # sll.delete_item(50)
    # print()
    # sll.print_list_items()
    # sll.delete_item(20)
    # print()
    # sll.print_list_items()
    # print()
    # sll.delete_item(30)
    # print()
    # sll.print_list_items()

    """ Elementary Operation Performance END """

    """ Iterable Printing using Iterator Implicitly  """
    # for item in sll:
    #     print(item)

    """ Iterable Printing using Iterator Explicitly  """
    # sll_iterator = sll.__iter__()
    # print(sll_iterator.__next__())

    """ Second way """
    # sll_iterator = iter(sll)
    # print(next(sll_iterator))
    # print(next(sll_iterator))
    # print(next(sll_iterator))
    # print(next(sll_iterator))
    # print(next(sll_iterator))
