
class Node:

    def __init__(self, prev=None, item=None, next=None) -> None:

        self.prev = prev
        self.item = item
        self.next = next


class CDLLL:

    def __init__(self) -> None:

        self.start = None

    def is_empty(self):

        return self.start == None

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):

        if not self.start or (self.current == self.start and hasattr(self, 'has_iterated')):
            raise StopIteration

        data = self.current.item
        self.current = self.current.next
        self.has_iterated = True
        return data

    def insert_at_start(self, item):

        node = Node(item=item)

        if self.is_empty():

            self.start = node
            self.start.next = node
            self.start.prev = node
        else:

            node.next = self.start
            node.prev = self.start.prev
            self.start.prev.next = node
            self.start.prev = node
            self.start = node

    def insert_at_last(self, item):

        node = Node(item=item)

        if self.is_empty():
            self.start = node
            self.start.next = node
            self.start.prev = node

        else:
            node.next = self.start
            node.prev = self.start.prev
            self.start.prev.next = node
            self.start.prev = node

    def search(self, item):

        if not self.is_empty():

            if self.start.item == item:
                return self.start

            elif self.start.prev.item == item:
                return self.start.prev

            else:
                temp = self.start.next

                while temp != self.start:
                    if temp.item == item:
                        return temp
                    temp = temp.next
        return None

    def get_index_of_node(self, item):

        if not self.is_empty():

            if self.start.item == item:
                return 1

            else:
                temp = self.start.next
                index = 2

                while temp != self.start:
                    if temp.item == item:
                        return index
                    temp = temp.next
                    index += 1
        return None

    def insert_after(self, insert_after_item, item_to_be_insert):
        node_info = self.search(insert_after_item)

        if node_info:

            if node_info == self.start.prev:
                self.insert_at_last(item_to_be_insert)

            else:
                node = Node(item=item_to_be_insert)
                node.next = node_info.next
                node.prev = node_info
                node_info.next.prev = node
                node_info.next = node

    def print_list_items(self):

        if not self.is_empty():
            temp = self.start

            while True:
                print(temp.item, end=' ')
                temp = temp.next
                if temp == self.start:
                    break
        print()

    def delete_first(self):

        if not self.is_empty():

            if self.start.next == self.start:
                self.start = None

            else:
                self.start.next.prev = self.start.prev
                self.start.prev.next = self.start.next
                self.start = self.start.next

    def delete_last(self):

        if not self.is_empty():

            if self.start.next == self.start:
                self.start = None

            else:

                self.start.prev = self.start.prev.prev
                self.start.prev.next = self.start

    def delete_item(self, item):

        node_info = self.search(item)

        if node_info:

            if node_info == self.start:
                self.delete_first()

            elif node_info == self.start.prev:
                self.delete_last()

            else:
                node_info.prev.next = node_info.next
                node_info.next.prev = node_info.prev


if __name__ == "__main__":

    cdll = CDLLL()

    """ Elementary Operation Performance START """

    # cdll.insert_at_start(30)
    # cdll.insert_at_start(20)
    # cdll.insert_at_start(10)

    # cdll.print_list_items()

    # cdll.insert_at_last(40)
    # cdll.insert_at_last(50)

    # print(cdll.search(10))
    # print(cdll.search(50))
    # print(cdll.search(30))
    # print(cdll.search(55))
    # print(cdll.get_index_of_node(20))

    # cdll.insert_after(10, 15)
    # cdll.insert_after(50, 55)
    # cdll.insert_after(30, 35)
    # cdll.print_list_items()

    # cdll.delete_first()
    # cdll.print_list_items()
    # cdll.delete_first()
    # cdll.print_list_items()
    # cdll.delete_first()
    # cdll.print_list_items()
    # cdll.delete_first()
    # cdll.print_list_items()
    # cdll.delete_first()
    # cdll.print_list_items()
    # cdll.delete_first()
    # cdll.print_list_items()
    # cdll.delete_first()
    # cdll.print_list_items()
    # cdll.delete_first()
    # cdll.print_list_items()

    # cdll.delete_last()
    # cdll.print_list_items()
    # cdll.delete_last()
    # cdll.print_list_items()
    # cdll.delete_last()
    # cdll.print_list_items()
    # cdll.delete_last()
    # cdll.print_list_items()
    # cdll.delete_last()
    # cdll.print_list_items()
    # cdll.delete_last()
    # cdll.print_list_items()
    # cdll.delete_last()
    # cdll.print_list_items()
    # cdll.delete_last()
    # cdll.print_list_items()

    # cdll.delete_item(10)
    # cdll.print_list_items()
    # cdll.delete_item(55)
    # cdll.print_list_items()
    # cdll.delete_item(30)
    # cdll.print_list_items()
    # cdll.delete_item(80)
    # cdll.print_list_items()

    """ Iterable Printing using Iterator Implicitly  """
    # for item in dcll:
    #     print(item)

    """ Iterable Printing using Iterator Explicitly  """
    # dcll_iterator = dcll.__iter__()
    # print(dcll_iterator.__next__())

    """ Second way """
    # dcll_iterator = iter(dcll)
    # print(next(dcll_iterator))
    # print(next(dcll_iterator))
    # print(next(dcll_iterator))
    # print(next(dcll_iterator))
    # print(next(dcll_iterator))
