
def enqueue(queue, value):
    queue.append(value)


def dequeue(queue):
    if len(queue) == 0:
        return None
    else:
        return queue.pop(0)


def peek(queue):
    if len(queue) == 0:
        return None
    else:
        return queue[-1]


def isempty(queue):
    if len(queue) == 0:
        return True
    else:
        return False


def multienqueue(queue, items):
    for item in items:
        enqueue(queue, item)


def multidequeue(queue, number):
    ls = []
    while number > 0:
        if isempty(queue) == False:
            ls.append(dequeue(queue))

        else:
            return ls

        number -= 1
    return ls









