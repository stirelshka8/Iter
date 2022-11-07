class FlatIterator:
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.len_list = len(self.list_of_list)
        self.main_list_cursor = 0
        self.nested_list_cursor = 0
        return self

    def __next__(self):


        return item


def test():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        print(flat_iterator_item)
        print(check_item)
        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test()
