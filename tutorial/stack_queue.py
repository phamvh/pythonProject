from collections import deque

if __name__ == '__main__':
    """
    Use list for a stack, because pop() method is efficient in popping the last element.
    However, list.pop() is not efficient in popping the first element because it needs to shift the entire array to the left.
    So, for queue, use deque instead. deque is fast in adding and popping from both ends 
    """

    lis = [1, 2, 3]
    lis.append(4) # add a element
    print(lis.pop())  # 4: the last added one got popped

    queue: deque[int] = deque()
    queue.append(1)
    queue.append(2)
    queue.appendleft(0)
    queue.append(3)

    print(queue.pop()) # 3 - the last added one on the right
    print(queue.popleft()) # 0 - the last added one on the left
