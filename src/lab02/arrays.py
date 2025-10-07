def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        raise ValueError("Список не может быть пустым")
    return min(nums), max(nums)

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

def flatten(mat: list[list | tuple]) -> list:
    result = []
    for item in mat:
        if not isinstance(item, (list,tuple)):
            raise TypeError(f'Элемент {item} не является списком/кортежем')
        result.extend(item)
    return result

print('min_max',
    min_max([3,-1,5,5,0]),
    min_max([42]),
    min_max([-5,-2,-9]),
    min_max([]),
    min_max([1.5,2,2.0,-3.1])
    )

print('unique_sorted',
    unique_sorted([3, 1, 2, 1, 3]),
    unique_sorted([]),
    unique_sorted([-1, -1, 0, 2, 2]),
    unique_sorted([1.0, 1, 2.5, 2.5, 0])
)

print('flatten',
    flatten([[1, 2], [3, 4]]),
    flatten([[1, 2], (3, 4, 5)] ),
    flatten([[1], [], [2, 3]]),
    flatten([[1, 2], "ab"])
)