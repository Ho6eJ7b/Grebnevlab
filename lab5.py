# import time
# def compute_lps(pattern):
#     lps = [0] * len(pattern)
#     length = 0
#     i = 1
#     while i < len(pattern):
#         if pattern[i] == pattern[length]:
#             length += 1
#             lps[i] = length
#             i += 1
#         else:
#             if length != 0:
#                 length = lps[length - 1]
#             else:
#                 lps[i] = 0
#                 i += 1
#     return lps
# def kmp_search(text, pattern, case_sensitive=True):
#     if not case_sensitive:
#         text = text.lower()
#         pattern = pattern.lower()
#     lps = compute_lps(pattern)
#     i = 0
#     j = 0
#     results = []
#     while i < len(text):
#         if pattern[j] == text[i]:
#             i += 1
#             j += 1
#         if j == len(pattern):
#             results.append(i - j)
#             j = lps[j - 1]
#         elif i < len(text) and pattern[j] != text[i]:
#             if j != 0:
#                 j = lps[j - 1]
#             else:
#                 i += 1
#     return results
# def boyer_moore_search(text, pattern, case_sensitive=True):
#     if not case_sensitive:
#         text = text.lower()
#         pattern = pattern.lower()
#     m = len(pattern)
#     n = len(text)
#     if m == 0:
#         return []
#     bad_char = {}
#     for i in range(m):
#         bad_char[pattern[i]] = i
#     results = []
#     s = 0
#     while s <= n - m:
#         j = m - 1
#         while j >= 0 and pattern[j] == text[s + j]:
#             j -= 1
#         if j < 0:
#             results.append(s)
#             s += (m - bad_char.get(text[s + m], -1) if s + m < n else 1)
#         else:
#             s += max(1, j - bad_char.get(text[s + j], -1))
#     return results
# def main():
#     text = input("строка: ")
#     pattern = input("подстрока: ")
#     case_option = input("регистр y/n? ").lower()
#     case_sensitive = case_option == 'y'
#     start_time = time.time()
#     kmp_result = kmp_search(text, pattern, case_sensitive)
#     kmp_time = time.time() - start_time
#     start_time = time.time()
#     bm_result = boyer_moore_search(text, pattern, case_sensitive)
#     bm_time = time.time() - start_time
#     start_time = time.time()
#     std_result = [i for i in range(len(text) - len(pattern) + 1) if text[i:i + len(pattern)] == pattern]
#     std_time = time.time() - start_time
#     print(f"\nрезультат:")
#     print(f"кмр: {kmp_result}")
#     print(f"мур: {bm_result}")
#     print(f"стандарт: {std_result}")
#     print(f"\nвремя:")
#     print(f"кмр: {kmp_time:.6f}")
#     print(f"мур: {bm_time:.6f}")
#     print(f"стандарт: {std_time:.6f}")
# if __name__ == "__main__":
#     main()

from collections import deque
def get_neighbors(state):
    neighbors = []
    size = int(len(state) ** 0.5)
    empty_pos = state.index(0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    row, col = divmod(empty_pos, size)
    for move in moves:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < size and 0 <= new_col < size:
            new_empty_pos = new_row * size + new_col
            new_state = list(state)
            new_state[empty_pos], new_state[new_empty_pos] = new_state[new_empty_pos], new_state[empty_pos]
            neighbors.append((new_state, new_empty_pos))

    return neighbors
def solve_puzzle(start_state):
    goal_state = tuple(range(1, len(start_state))) + (0,)
    start_state = tuple(start_state)
    if start_state == goal_state:
        return []
    queue = deque([(start_state, [], start_state.index(0))])
    visited = set()
    visited.add(start_state)
    while queue:
        state, path, empty_pos = queue.popleft()
        for neighbor_state, new_empty_pos in get_neighbors(state):
            if neighbor_state not in visited:
                visited.add(neighbor_state)
                new_path = path + [state[new_empty_pos]]
                if neighbor_state == goal_state:
                    return new_path
                queue.append((neighbor_state, new_path, new_empty_pos))
    return []
if __name__ == "__main__":
    start_state = list(map(int, input("состояние: ").split()))
    result = solve_puzzle(start_state)
    if result:
        print("победа, шаги", result)
    else:
        print("невозможно.")
