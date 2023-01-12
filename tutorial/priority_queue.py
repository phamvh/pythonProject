import heapq

if __name__ == '__main__':
    """
    Use heapq module for priority queues in Python. It is a min heap.
    It operates on a given list, so every method needs to take a list as one of the args.
    It has only 5 functions:
    1. heapify: need to call this function first to create a heap on a given list
    2. Then call: heappop, heappush, etc.
    
    Note: this is a min heap.
    To get a max heap, simply invert number to negative, such as 100 -> -100, before pushing into the heap.
    """
    lis = [3,4,1,5,8,2]
    heapq.heapify(lis)
    print(lis) # [1, 4, 2, 5, 8, 3]

    print(heapq.heappop(lis)) # 1
    print(lis) # [2, 4, 3, 5, 8]

    heapq.heappush(lis, 0)
    print(lis) # [0, 4, 2, 5, 8, 3]

    print(heapq.heappushpop(lis, 1)) # 0:  push an item, and pop and returned that popped item
    print(lis) # [1, 4, 2, 5, 8, 3]

    three_smallest = heapq.nsmallest(3, lis) # get 3 smallest, not modifying the heap
    print(three_smallest) # [1, 2, 3]
    three_largest = heapq.nlargest(3, lis)
    print(three_largest) # [8, 5, 4]

    print(lis) # heap remains the same
    smallest = heapq.heapreplace(lis, 8) # first pop the smallest, and add new item (8), and return the smallest
    print(smallest) # 1

