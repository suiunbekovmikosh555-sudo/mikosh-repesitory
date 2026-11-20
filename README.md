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


19 задача
def is_interesting(number: int, awesome_phrases: list[int]) -> int:
    def check_single(n: int) -> bool:
        if n < 100:
            return False

        s = str(n)

        # 1. Any digit followed by all zeros
        if len(set(s[1:])) == 1 and s[1] == "0":
            return True

        # 2. Every digit is the same
        if len(set(s)) == 1:
            return True

        # 3. Sequential incrementing (0 comes after 9, not before 1)
        inc_pattern = "1234567890"
        if s in inc_pattern:
            return True

        # 4. Sequential decrementing (0 comes after 1, not before 9)
        dec_pattern = "9876543210"
        if s in dec_pattern:
            return True

        # 5. Palindrome
        if s == s[::-1]:
            return True

        # 6. Matches awesome_phrases
        if n in awesome_phrases:
            return True

        return False

    if check_single(number):
        return 2
    if check_single(number + 1) or check_single(number + 2):
        return 1
    return 0
    
20 задача
def doubles(maxk: int, maxn: int) -> float:
    total = 0.0
    for n in range(2, maxn + 2):
        inv_sq = 1.0 / (n * n)
        power = inv_sq  # equals (n)^(-2*k) for k = 1
        for k in range(1, maxk + 1):
            term = power / k
            if term == 0.0:
                break
            total += term
            power *= inv_sq
    return total


21 задача
from __future__ import annotations


def _is_valid(board: list[list[int]], row: int, col: int, num: int) -> bool:
    # Check row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                return False

    return True


def _solve_in_place(board: list[list[int]]) -> bool:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if _is_valid(board, row, col, num):
                        board[row][col] = num
                        if _solve_in_place(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def sudoku(puzzle: list[list[int]]) -> list[list[int]]:
    board = [row[:] for row in puzzle]
    if not _solve_in_place(board):
        raise ValueError("No valid Sudoku solution exists for the given puzzle.")
    return board


if __name__ == "__main__":
    puzzle = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    solved = sudoku(puzzle)
    for row in solved:
        print(row)


22 задача
from __future__ import annotations

from collections import defaultdict


def calculate(rectangles: list[list[int]]) -> int:
    if not rectangles:
        return 0

    # Group y-interval changes by x coordinate: (y0, y1, delta)
    events_by_x: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
    for x0, y0, x1, y1 in rectangles:
        if x0 < x1 and y0 < y1:
            events_by_x[x0].append((y0, y1, 1))
            events_by_x[x1].append((y0, y1, -1))

    if not events_by_x:
        return 0

    sorted_xs = sorted(events_by_x)
    active_counts: dict[tuple[int, int], int] = defaultdict(int)
    total_area = 0
    prev_x = sorted_xs[0]

    for x in sorted_xs:
        dx = x - prev_x
        if dx > 0 and active_counts:
            # Compute total length of union of active [y0, y1] intervals
            intervals = sorted(active_counts.keys())
            covered_y = 0
            cur_start, cur_end = intervals[0]

            for y0, y1 in intervals[1:]:
                if y0 <= cur_end:
                    if y1 > cur_end:
                        cur_end = y1
                else:
                    covered_y += cur_end - cur_start
                    cur_start, cur_end = y0, y1

            covered_y += cur_end - cur_start
            total_area += dx * covered_y

        # Apply all events at current x
        for y0, y1, delta in events_by_x[x]:
            new_count = active_counts[(y0, y1)] + delta
            if new_count > 0:
                active_counts[(y0, y1)] = new_count
            else:
                del active_counts[(y0, y1)]

        prev_x = x

    return total_area


if __name__ == "__main__":
    rects = [
        [3, 3, 8, 5],
        [6, 3, 8, 9],
        [11, 6, 14, 12],
    ]
    print(calculate(rects))  # 36


23 задача 
from __future__ import annotations

import heapq


def cheapest_path(
    t: list[list[int]],
    start: tuple[int, int],
    finish: tuple[int, int],
) -> list[str]:
    if start == finish:
        return []

    rows = len(t)
    cols = len(t[0])

    moves: tuple[tuple[int, int, str], ...] = (
        (-1, 0, "up"),
        (1, 0, "down"),
        (0, -1, "left"),
        (0, 1, "right"),
    )

    dist: dict[tuple[int, int], int] = {start: 0}
    # Храним: (current_cell, direction_from_parent)
    parent: dict[tuple[int, int], tuple[tuple[int, int], str]] = {}
    pq: list[tuple[int, int, int]] = [(0, start[0], start[1])]

    while pq:
        cost, r, c = heapq.heappop(pq)
        curr = (r, c)

        if curr == finish:
            break

        if cost > dist.get(curr, float("inf")):
            continue

        step_cost = t[r][c]
        for dr, dc, direction in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                nxt = (nr, nc)
                new_cost = cost + step_cost
                if new_cost < dist.get(nxt, float("inf")):
                    dist[nxt] = new_cost
                    parent[nxt] = (curr, direction)
                    heapq.heappush(pq, (new_cost, nr, nc))

    if finish not in parent:
        return []

    path: list[str] = []
    node = finish
    while node != start:
        prev_node, direction = parent[node]
        path.append(direction)
        node = prev_node

    path.reverse()
    return path


if __name__ == "__main__":
    toll_map = [
        [1, 9, 1],
        [2, 9, 1],
        [2, 1, 1],
    ]
    print(cheapest_path(toll_map, (0, 0), (0, 2)))


24 задача
from __future__ import annotations

POINTS: dict[str, tuple[int, int]] = {
    "A": (0, 0), "B": (0, 1), "C": (0, 2),
    "D": (1, 0), "E": (1, 1), "F": (1, 2),
    "G": (2, 0), "H": (2, 1), "I": (2, 2),
}

ALL_COORDS: tuple[tuple[int, int], ...] = tuple(POINTS.values())


def _can_move(
    cur: tuple[int, int],
    nxt: tuple[int, int],
    visited: set[tuple[int, int]],
) -> bool:
    if nxt in visited:
        return False

    r1, c1 = cur
    r2, c2 = nxt
    sum_r = r1 + r2
    sum_c = c1 + c2

    # Промежуточная точка существует, когда обе координаты середины целые
    if sum_r % 2 == 0 and sum_c % 2 == 0:
        mid = (sum_r // 2, sum_c // 2)
        if mid != cur and mid != nxt and mid not in visited:
            return False

    return True


def count_patterns_from(first_point: str, length: int) -> int:
    if length <= 0 or length > 9 or first_point not in POINTS:
        return 0
    if length == 1:
        return 1

    start = POINTS[first_point]

    def dfs(curr: tuple[int, int], remaining: int, visited: set[tuple[int, int]]) -> int:
        if remaining == 0:
            return 1

        total = 0
        for nxt in ALL_COORDS:
            if _can_move(curr, nxt, visited):
                visited.add(nxt)
                total += dfs(nxt, remaining - 1, visited)
                visited.remove(nxt)
        return total

    return dfs(start, length - 1, {start})


# Алиас под именование в условии задачи
countPatternsFrom = count_patterns_from


if __name__ == "__main__":
    print(count_patterns_from("C", 2))  # 5
    # Проверка всех допустимых длин 4..9 для Android (ожидается 389112)
    total_android = sum(
        count_patterns_from(pt, length)
        for pt in POINTS
        for length in range(4, 10)
    )
    print("Всего ключей (4..9):", total_android


25 задача
def line(grid):
    if not grid or not grid[0]:
        return False

    h = len(grid)
    w = len(grid[0])

    endpoints = []
    total_line_chars = 0

    for r in range(h):
        for c in range(w):
            ch = grid[r][c]
            if ch == "X":
                endpoints.append((r, c))
                total_line_chars += 1
            elif ch in ("-", "|", "+"):
                total_line_chars += 1

    if len(endpoints) != 2:
        return False

    def can_enter(nr, nc, dr, dc, target_end):
        if not (0 <= nr < h and 0 <= nc < w):
            return False
        nch = grid[nr][nc]
        if (nr, nc) == target_end:
            return True
        if dr != 0:  # moving vertically
            return nch in ("|", "+")
        if dc != 0:  # moving horizontally
            return nch in ("-", "+")
        return False

    def trace(start, end):
        visited = {start}
        r, c = start

        # Initial step from starting 'X'
        initial_moves = []
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr, nc = r + dr, c + dc
            if (nr, nc) not in visited and can_enter(nr, nc, dr, dc, end):
                initial_moves.append((nr, nc, dr, dc))

        # Must have a single unambiguous starting direction
        if len(initial_moves) != 1:
            return False

        r, c, dr, dc = initial_moves[0]
        visited.add((r, c))

        while (r, c) != end:
            ch = grid[r][c]

            if ch == "-":
                if dr != 0:
                    return False
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited or not can_enter(nr, nc, dr, dc, end):
                    return False
                r, c = nr, nc
                visited.add((r, c))

            elif ch == "|":
                if dc != 0:
                    return False
                nr, nc = r + dr, c + dc
                if (nr, nc) in visited or not can_enter(nr, nc, dr, dc, end):
                    return False
                r, c = nr, nc
                visited.add((r, c))

            elif ch == "+":
                # Must turn 90 degrees
                turn_dirs = ((-1, 0), (1, 0)) if dr == 0 else ((0, -1), (0, 1))
                next_moves = []
                for ndr, ndc in turn_dirs:
                    nr, nc = r + ndr, c + ndc
                    if (nr, nc) not in visited and can_enter(nr, nc, ndr, ndc, end):
                        next_moves.append((nr, nc, ndr, ndc))

                if len(next_moves) != 1:
                    return False

                r, c, dr, dc = next_moves[0]
                visited.add((r, c))

            else:
                return False

        return len(visited) == total_line_chars

    p1, p2 = endpoints
    return trace(p1, p2) or trace(p2, p1)


26 задача
def validate_battlefield(field: list[list[int]]) -> bool:
    if len(field) != 10 or any(len(row) != 10 for row in field):
        return False

    total_ones = sum(sum(row) for row in field)
    if total_ones != 20:
        return False

    used = [[False] * 10 for _ in range(10)]
    # size -> remaining count: 1 battleship (4), 2 cruisers (3), 3 destroyers (2), 4 submarines (1)
    remaining = {4: 1, 3: 2, 2: 3, 1: 4}

    def find_next_cell() -> tuple[int, int] | None:
        for r in range(10):
            for c in range(10):
                if field[r][c] == 1 and not used[r][c]:
                    return r, c
        return None

    def backtrack(covered: int) -> bool:
        if covered == 20:
            return all(cnt == 0 for cnt in remaining.values())

        nxt = find_next_cell()
        if nxt is None:
            return False

        r, c = nxt

        for size in (4, 3, 2, 1):
            if remaining[size] == 0:
                continue

            if size == 1:
                used[r][c] = True
                remaining[1] -= 1
                if backtrack(covered + 1):
                    return True
                remaining[1] += 1
                used[r][c] = False
            else:
                # Try horizontal placement to the right
                if c + size <= 10 and all(
                    field[r][c + k] == 1 and not used[r][c + k] for k in range(size)
                ):
                    for k in range(size):
                        used[r][c + k] = True
                    remaining[size] -= 1

                    if backtrack(covered + size):
                        return True

                    remaining[size] += 1
                    for k in range(size):
                        used[r][c + k] = False

                # Try vertical placement downwards
                if r + size <= 10 and all(
                    field[r + k][c] == 1 and not used[r + k][c] for k in range(size)
                ):
                    for k in range(size):
                        used[r + k][c] = True
                    remaining[size] -= 1

                    if backtrack(covered + size):
                        return True

                    remaining[size] += 1
                    for k in range(size):
                        used[r + k][c] = False

        return False

    return backtrack(0)


27 задача
import math


class Blobservation:
    def __init__(self, h: int, w: int | None = None) -> None:
        if not self._is_valid_int(h) or not (8 <= h <= 50):
            raise ValueError("h must be an integer between 8 and 50.")
        if w is None:
            w = h
        if not self._is_valid_int(w) or not (8 <= w <= 50):
            raise ValueError("w must be an integer between 8 and 50.")

        self.h: int = h
        self.w: int = w
        # Map (x, y) -> total size
        self._blobs: dict[tuple[int, int], int] = {}

    @staticmethod
    def _is_valid_int(value: object) -> bool:
        return isinstance(value, int) and not isinstance(value, bool)

    def populate(self, blobs: list[dict[str, int]]) -> None:
        if not isinstance(blobs, list):
            raise TypeError("blobs must be a list of dictionaries.")

        validated: list[tuple[int, int, int]] = []
        for item in blobs:
            if not isinstance(item, dict):
                raise TypeError("Each blob entry must be a dictionary.")
            if not {"x", "y", "size"}.issubset(item.keys()):
                raise ValueError("Each blob dictionary must contain 'x', 'y', and 'size'.")

            x = item["x"]
            y = item["y"]
            size = item["size"]

            if not (self._is_valid_int(x) and self._is_valid_int(y) and self._is_valid_int(size)):
                raise TypeError("'x', 'y', and 'size' must be integers (not booleans).")

            if not (0 <= x < self.h and 0 <= y < self.w):
                raise ValueError(f"Coordinates ({x}, {y}) are out of bounds for {self.h}x{self.w}.")

            if not (1 <= size <= 20):
                raise ValueError("Initial blob size must be between 1 and 20.")

            validated.append((x, y, size))

        # Apply all changes only after full validation succeeds
        for x, y, size in validated:
            self._blobs[(x, y)] = self._blobs.get((x, y), 0) + size

    @staticmethod
    def _clockwise_angle(bx: int, by: int, tx: int, ty: int) -> float:
        # 12 o'clock is dx = -1, dy = 0; x grows downward, y grows rightward
        dx = tx - bx
        dy = ty - by
        return math.atan2(dy, -dx) % (2.0 * math.pi)

    def _step_once(self) -> None:
        if len(self._blobs) <= 1:
            return

        sizes = self._blobs.values()
        min_size = min(sizes)
        max_size = max(sizes)
        if min_size == max_size:
            return

        items = list(self._blobs.items())  # [((x, y), size), ...]
        next_blobs: dict[tuple[int, int], int] = {}

        for (bx, by), b_size in items:
            if b_size <= min_size:
                next_blobs[(bx, by)] = next_blobs.get((bx, by), 0) + b_size
                continue

            targets = [
                ((tx, ty), t_size)
                for (tx, ty), t_size in items
                if t_size < b_size
            ]

            if not targets:
                next_blobs[(bx, by)] = next_blobs.get((bx, by), 0) + b_size
                continue

            # Best target: shortest distance, then largest size, then clockwise from 12:00
            (tx, ty), _ = min(
                targets,
                key=lambda item: (
                    max(abs(item[0][0] - bx), abs(item[0][1] - by)),
                    -item[1],
                    self._clockwise_angle(bx, by, item[0][0], item[0][1]),
                ),
            )

            step_x = 0 if tx == bx else (1 if tx > bx else -1)
            step_y = 0 if ty == by else (1 if ty > by else -1)
            nx, ny = bx + step_x, by + step_y

            next_blobs[(nx, ny)] = next_blobs.get((nx, ny), 0) + b_size

        self._blobs = next_blobs

    def move(self, steps: int = 1) -> None:
        if not self._is_valid_int(steps) or steps < 1:
            raise ValueError("steps must be a positive integer.")

        for _ in range(steps):
            if len(self._blobs) <= 1:
                break
            sizes = self._blobs.values()
            if min(sizes) == max(sizes):
                break
            self._step_once()

    def print_state(self) -> list[list[int]]:
        return [
            [x, y, size]
            for (x, y), size in sorted(self._blobs.items(), key=lambda kv: (kv[0][0], kv[0][1]))
        ]
