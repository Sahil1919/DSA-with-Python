
class Node:

    def __init__(self, item=None, next=None) -> None:
        self.item = item
        self.next = next


class CLL:

    def __init__(self) -> None:

        self.last = None

    def __iter__(self):
        if self.last:
            self.current = self.last.next
        return self

    def __next__(self):

        if not self.last or (self.current == self.last.next and hasattr(self, 'has_iterated')):
            raise StopIteration

        data = self.current.item
        self.current = self.current.next
        self.has_iterated = True
        return data

    def is_empty(self):

        return self.last == None

    def insert_at_start(self, item):

        node = Node(item)

        if self.is_empty():
            node.next = node
            self.last = node

        else:

            node.next = self.last.next
            self.last.next = node

    def insert_at_last(self, item):

        node = Node(item)

        if self.is_empty():
            node.next = node
            self.last = node

        else:

            node.next = self.last.next
            self.last.next = node
            self.last = node

    def search(self, item):

        if not self.is_empty():

            if item == self.last.item:
                return self.last

            elif item == self.last.next.item:
                return self.last.next

            else:
                temp = self.last.next

                while temp != self.last:
                    if temp.item == item:
                        return temp
                    temp = temp.next

        return None

    def get_index_of_node(self, item):

        temp = self.last.next
        index = 1

        while temp and temp != self.last:
            if temp.item == item:
                return index

            temp = temp.next
            index += 1

        return -1

    def insert_after(self, insert_after_item, item_to_be_insert):
        node = self.search(insert_after_item)

        if node:
            if node == self.last:
                self.insert_at_last(item_to_be_insert)
            else:
                node.next = Node(item_to_be_insert, node.next)

    def print_list_items(self):

        if not self.is_empty():
            temp = self.last.next

            while True:
                print(temp.item, end=' ')
                if temp == self.last:
                    break
                temp = temp.next

            print()

    def delete_first(self):

        if not self.is_empty():

            if self.last == self.last.next:
                self.last = None

            else:
                self.last.next = self.last.next.next

    def delete_last(self):

        if not self.is_empty():

            if self.last == self.last.next:
                self.last = None

            else:
                temp = self.last

                while temp.next != self.last:
                    temp = temp.next

                temp.next = self.last.next
                self.last = temp

    def delete_item(self, item):

        node = self.search(item)

        if node:

            if node == self.last:
                self.delete_last()

            elif node == self.last.next:
                self.delete_first()

            else:
                temp = self.last.next

                while temp.next != self.last:
                    if temp.next.item != item:
                        temp = temp.next
                    else:
                        break

                temp.next = temp.next.next


if __name__ == "__main__":

    cll = CLL()

    """ Elementary Operation Performance START """
    # cll.insert_at_start(20)
    # cll.insert_at_start(10)

    # cll.insert_at_last(30)
    # cll.insert_at_last(40)
    # cll.print_list_items()

    # print(cll.search(40).item)
    # print(cll.search(10).item)
    # print(cll.search(30).item)
    # print(cll.search(45))

    # print(cll.get_index_of_node(30))
    # print(cll.get_index_of_node(40))

    # cll.insert_after(40, 50)
    # cll.insert_after(10, 15)
    # cll.insert_after(30, 35)
    # cll.print_list_items()

    # cll.delete_first()
    # cll.print_list_items()

    # cll.delete_last()
    # cll.print_list_items()

    # cll.delete_item(30)
    # cll.print_list_items()
    # cll.delete_item(20)
    # cll.print_list_items()
    
    """ Elementary Operation Performance END """

    """ Iterable Printing using Iterator Implicitly  """
    # for item in cll:
    #     print(item)

    """ Iterable Printing using Iterator Explicitly  """
    # cll_iterator = cll.__iter__()
    # print(cll_iterator.__next__())

    """ Second way """
    # cll_iterator = iter(cll)
    # print(next(cll_iterator))
    # print(next(cll_iterator))
    # print(next(cll_iterator))
    # print(next(cll_iterator))
    # print(next(cll_iterator))