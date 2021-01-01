import time

unsorted_items = [23, 19, 20, 34, 24, 26, 13, 30, 34, 31,
                  30, 20, 35, 14, 22, 20, 21, 31, 28, 16,
                  30, 13, 7, 11, 32, 0, 34, 1, 12, 6, 30, 6, 30, 33, 13]


def timing_decorator(func):
    def wrapper(unsorted=None):
        start = time.time()
        func(unsorted)
        end = time.time()
        print(func.__name__, end - start)

    return wrapper


@timing_decorator
def bubble_sort(unsorted=None):
    if not unsorted:
        unsorted = list(unsorted_items)

    while True:
        sorted_count = 0
        for i in range(len(unsorted) - 1):
            if unsorted[i] > unsorted[i + 1]:
                unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                continue  # if i put 'break' here the sorting will become stupid
            sorted_count += 1
            if sorted_count == (len(unsorted) - 1):
                return unsorted


@timing_decorator
def cocktail_sort(unsorted=None):
    if not unsorted:
        unsorted = list(unsorted_items)
    i = int()
    is_forward = bool()
    sorted_count = int()

    while True:
        if i == 0:
            is_forward = True
            sorted_count = 0
        if i == (len(unsorted) - 1):
            is_forward = False
            sorted_count = 0

        if is_forward:
            if unsorted[i] > unsorted[i + 1]:
                unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
            else:
                sorted_count += 1
            i += 1
            continue

        if unsorted[i] < unsorted[i - 1]:
            unsorted[i], unsorted[i - 1] = unsorted[i - 1], unsorted[i]
        else:
            sorted_count += 1
        i -= 1

        if sorted_count == (len(unsorted) - 1):
            return unsorted


@timing_decorator
def even_odd_sort(unsorted=None):
    if not unsorted:
        unsorted = list(unsorted_items)
    is_even = bool()

    while True:
        sorted_count = 0
        for i in range(len(unsorted) - 1):
            if is_even:
                if i % 2 == 0:
                    if unsorted[i] > unsorted[i + 1]:
                        unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                    else:
                        sorted_count += 1
                    continue
            if i % 2 == 1:
                if unsorted[i] > unsorted[i + 1]:
                    unsorted[i], unsorted[i + 1] = unsorted[i + 1], unsorted[i]
                else:
                    sorted_count += 1

        if sorted_count == (len(unsorted) - 1):
            return unsorted

        is_even = not is_even


@timing_decorator
def comb_sort(unsorted=None):
    if not unsorted:
        unsorted = list(unsorted_items)
    shrink_factor = 1.247
    interval = len(unsorted)

    while True:
        interval = int(interval / shrink_factor)
        for i in range(len(unsorted) - 1):
            if interval == 1:
                return bubble_sort(unsorted)
            if unsorted[i] > unsorted[i + interval]:
                unsorted[i], unsorted[i + interval] = unsorted[i + interval], unsorted[i]

            interval = int(interval / shrink_factor)

if __name__ == '__main__':
    bubble_sort()
    cocktail_sort()
    even_odd_sort()
    comb_sort()
    pass
