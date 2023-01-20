"""
Failed to install ordered_set. It suggested running the following in the terminal:
source /Users/huypham/PycharmProjects/pythonProject/venv/bin/activate
pip install OrderedSet

Tried in the terminal, and it was actually named "ordered-set". Command should be:
source /Users/huypham/PycharmProjects/pythonProject/venv/bin/activate
pip install ordered-set
"""
if __name__ == '__main__':
    from ordered_set import OrderedSet
    set1 = OrderedSet([2,1,4,2,9,3])
    for x in set1:
        print(x, end=", ") #2, 1, 4, 9, 3,  same order as in the init list

    print()

    set2 = set([2, 1, 4, 2, 9, 3])
    for x in set2:
        print(x, end=", ") # 1, 2, 3, 4, 9,  # different order, looks sorted


    print()
    # dict in python3 is ordered, but not in python 2. In python2, one needs to use OrderedDict
    d = {1: "one", 5: "five", 3: "three", 2: "two", 8: "eight", 9: "nine"}
    for x in d.items():
        print(x, end= ", ") # (1, 'one'), (5, 'five'), (3, 'three'), (2, 'two'), (8, 'eight'), (9, 'nine'),
        print(type(x)) # <class 'tuple'> x is a tuple actually