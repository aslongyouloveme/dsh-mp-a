"""A simple insertion sort for lists of comparable values."""


def insertion_sort(values):
    """Return a new list in ascending order without changing values.

    Insertion sort is stable, takes O(n²) time in the worst case,
    and uses O(n) extra space to preserve the input.
    """
    result = list(values)
    for index in range(1, len(result)):
        value = result[index]
        position = index
        while position > 0 and result[position - 1] > value:
            result[position] = result[position - 1]
            position -= 1
        result[position] = value
    return result
