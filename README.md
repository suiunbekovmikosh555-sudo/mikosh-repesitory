# mikosh-repesitory
1 задача 
def binary_array_to_number(arr):
    return int("".join(str(bit) for bit in arr), 2)


2 задача 
def create_phone_number(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


 3 задача
 def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        # Эгер кийинки тамганын коду мурункусунан 1ге чоң болбосо, демек ошол арадагы тамга жетишпейт
        if ord(chars[i + 1]) - ord(chars[i]) > 1:
            return chr(ord(chars[i]) +


4 задача
def get_middle(s):
    length = len(s)
    middle = length // 2
    if length % 2 == 0:
        return s[middle - 1 : middle + 1]
    else:
      
        
 5 задача       
 return s[middle]
def square_digits(num):
    return int("".join(str(int(digit) ** 2) for digit in str(num)))


def sort_array(source_array):
    # Массивдеги бардык так сандарды тандап, аларды өсүш тартибинде сорттойбуз
    odds = sorted([x for x in source_array if x % 2 != 0])
    
6 задача    # Так сандарды сактоо үчүн индекс
    odd_index = 0
    # Жыйынтык үчүн тизме түзөбүз
    result = []
    for x in source_array:
        if x % 2 != 0:
            result.append(odds[odd_index])
            odd_index += 1
        else:
            result.append(x)
            
return result
  

def max_sequence(arr):
    max_sum = 0
    current_sum = 0

 7 задача
 for num in arr:
        current_sum = max(0, current_sum + num)
        max_sum = max(max_sum, current_sum)

    
return max_sum


8 задача
def find_even_index(arr):
    total = sum(arr)
    left_sum = 0

    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]

        if left_sum == right_sum:
            return i

        left_sum += arr[i]

    return -1


задача 9
def high(x):
    words = x.split()
    return max(words, key=lambda word: sum(ord(c) - ord('a') + 1 for c in word))


10 задача
class RomanNumerals:
    @staticmethod
    def to_roman(val: int) -> str:
        values = [
            (1000, "M"), (900, "CM"), (500, "D"),
            (400, "CD"), (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"), (10, "X"),
            (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        result = ""

        for number, symbol in values:
            while val >= number:
                result += symbol
                val -= number

        return result

    @staticmethod
    def from_roman(roman_num: str) -> int:
        values = {
            "M": 1000, "D": 500, "C": 100,
            "L": 50, "X": 10, "V": 5, "I": 1
        }

        total = 0

        for i in range(len(roman_num)):
            if i + 1 < len(roman_num) and values[roman_num[i]] < values[roman_num[i + 1]]:
                total -= values[roman_num[i]]
            else:
                total += values[roman_num[i]]

        return total


11 задача
def get_pins(observed):
    neighbors = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9']
    }

    result = ['']

    for digit in observed:
        result = [prefix + neighbor for prefix in result
                  for neighbor in neighbors[digit]]

    return result


12 задача
def sum_of_intervals(intervals):
    if not intervals:
        return 0

    intervals = sorted(intervals)
    total = 0

    start, end = intervals[0]

    for a, b in intervals[1:]:
        if a <= end:
            end = max(end, b)
        else:
            total += end - start
            start, end = a, b

    total += end - start
    return total


задача 13
def int32_to_ip(int32):
    return ".".join(str((int32 >> (8 * i)) & 255) for i in range(3, -1, -1))


14 задача
def order_weight(strng):
    return " ".join(sorted(strng.split(), key=lambda x: (sum(int(d) for d in x), x)))

15 задача
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity_rank):
        valid_ranks = [-8, -7, -6, -5, -4, -3, -2, -1,
                       1, 2, 3, 4, 5, 6, 7, 8]

        if activity_rank not in valid_ranks:
            raise ValueError("Invalid rank")

        if self.rank == 8:
            return

        rank_index = valid_ranks.index(self.rank)
        activity_index = valid_ranks.index(activity_rank)
        difference = activity_index - rank_index

        if difference == 0:
            self.progress += 3
        elif difference == -1:
            self.progress += 1
        elif difference > 0:
            self.progress += 10 * difference * difference

        while self.progress >= 100 and self.rank < 8:
            self.progress -= 100
            self.rank = valid_ranks[valid_ranks.index(self.rank) + 1]

        if self.rank == 8:
            self.progress = 0


16 задача
def tree_by_levels(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        result.append(node.value)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return result


17 задача
def spiralize(size):
    grid = [[0] * size for _ in range(size)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    r, c = 0, 0
    d = 0

    while True:
        grid[r][c] = 1

        dr, dc = directions[d]
        nr, nc = r + dr, c + dc

        def safe(rr, cc):
            if not (0 <= rr < size and 0 <= cc < size):
                return False
            if grid[rr][cc]:
                return False

            for dr, dc in directions:
                ar, ac = rr + dr, cc + dc
                if 0 <= ar < size and 0 <= ac < size:
                    if grid[ar][ac] and (ar, ac) != (r, c):
                        return False

            return True

        if not safe(nr, nc):
            d = (d + 1) % 4
            dr, dc = directions[d]
            nr, nc = r + dr, c + dc

            if not safe(nr, nc):
                break

        r, c = nr, nc

    return grid


18 задача 
from collections import deque

def path_finder(maze):
    maze = maze.split("\n")
    n = len(maze)

    queue = deque([(0, 0)])
    visited = {(0, 0)}

    while queue:
        x, y = queue.popleft()

        if (x, y) == (n - 1, n - 1):
            return True

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if maze[nx][ny] == "." and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return False
