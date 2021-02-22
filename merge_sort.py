"""
    Python implementation of a sort algorithm.
    Best case scenario : O(n)
    Worst case scenario : O(n ^ 2) because native functions : min, max and remove are
    already O(n)
"""

def merge_sort(collection):
    """
        Pure implementation of the fastest ordered collection with heterogeneous

        : parameter collection : some mutable ordered collection with heterogeneous
        comparable items inside
        : return : a sollectiojn order by ascending

        Examples :
        >>> merge_sort([0, 5, 3, 2, 2])
        [0, 2, 2, 3, 5]

        >>> merge_sort([])
        []

        >>> merge_sort([-45, -5, -2])
        [-45, -5, -2]
    """

    start, end = [], []
    while len(collection) > 1 :
        min_one, max_one = min(collection), max(collection)
        start.append(min_one)
        end.append(max_one)
        collection.remove(min_one)
        collection.remove(max_one)
    end.reverse()
    return start + collection + end

if __name__ == "__main__" :
    user_input = input("Enter numbers separated by comma : \n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(merge_sort(unsorted), sep=",")