import random
import timeit
# def gen(size, start=0, end=10000):
#     return sorted(random.sample(range(start, end), size))
# def bin(arr, x):
#     l, r = 0, len(arr) - 1
#     while l <= r:
#         m = (l + r) // 2
#         if arr[m] == x:
#             return m
#         elif arr[m] < x:
#             l = m + 1
#         else:
#             r = m - 1
#     return -1
# class Node:
#     def __init__(self, key):
#         self.key = key
#         self.left = self.right = None
# class BST:
#     def __init__(self):
#         self.root = None
#     def insert(self, key):
#         def _insert(node, key):
#             if not node:
#                 return Node(key)
#             if key < node.key:
#                 node.left = _insert(node.left, key)
#             else:
#                 node.right = _insert(node.right, key)
#             return node
#         self.root = _insert(self.root, key)
#     def search(self, key):
#         def _search(node, key):
#             if not node or node.key == key:
#                 return node is not None
#             return _search(node.left, key) if key < node.key else _search(node.right, key)
#         return _search(self.root, key)
#     def delete(self, key):
#         def _min_value_node(node):
#             current = node
#             while current.left:
#                 current = current.left
#             return current
#         def _delete(node, key):
#             if not node:
#                 return node
#             if key < node.key:
#                 node.left = _delete(node.left, key)
#             elif key > node.key:
#                 node.right = _delete(node.right, key)
#             else:
#                 if not node.left:
#                     return node.right
#                 elif not node.right:
#                     return node.left
#                 temp = _min_value_node(node.right)
#                 node.key = temp.key
#                 node.right = _delete(node.right, temp.key)
#             return node
#         self.root = _delete(self.root, key)
# def bst(arr):
#     tree = BST()
#     def _build(start, end):
#         if start > end:
#             return
#         mid = (start + end) // 2
#         tree.insert(arr[mid])
#         _build(start, mid - 1)
#         _build(mid + 1, end)
#     _build(0, len(arr) - 1)
#     return tree
# def fib(arr, x):
#     n = len(arr)
#     fib2, fib1 = 0, 1
#     fib = fib1 + fib2
#     while fib < n:
#         fib2, fib1 = fib1, fib
#         fib = fib1 + fib2
#     offset = -1
#     while fib > 1:
#         i = min(offset + fib2, n - 1)
#         if arr[i] < x:
#             fib = fib1
#             fib1 = fib2
#             fib2 = fib - fib1
#             offset = i
#         elif arr[i] > x:
#             fib = fib2
#             fib1 = fib1 - fib2
#             fib2 = fib - fib1
#         else:
#             return i
#     if fib1 and offset + 1 < n and arr[offset + 1] == x:
#         return offset + 1
#     return -1
#
# def inter(arr, x):
#     low, hi = 0, len(arr) - 1
#     while low <= hi and arr[low] <= x <= arr[hi]:
#         if arr[hi] == arr[low]:
#             if arr[low] == x:
#                 return low
#             else:
#                 return -1
#         pos = low + ((hi - low) * (x - arr[low])) // (arr[hi] - arr[low])
#         if pos >= len(arr): return -1
#         if arr[pos] == x:
#             return pos
#         elif arr[pos] < x:
#             low = pos + 1
#         else:
#             hi = pos - 1
#     return -1
# def test_search_algorithms():
#     arr = gen(1000)
#     tree = bst(arr)
#     target = arr[len(arr)//2]
#     print("элемент:", target)
#     print("бинарынй:", timeit.timeit(lambda: bin(arr, target), number=1000))
#     print("дерево:", timeit.timeit(lambda: tree.search(target), number=1000))
#     print("фибоначчиев:", timeit.timeit(lambda: fib(arr, target), number=1000))
#     print("интерполяционный:", timeit.timeit(lambda: inter(arr, target), number=1000))
#     print("питон:", timeit.timeit(lambda: target in arr, number=1000))
# if __name__ == "__main__":
#     test_search_algorithms()




# TABLE_SIZE = 1000
# class Table1:
#     def __init__(self):
#         self.table = [None] * TABLE_SIZE
#     def insert(self, key):
#         index = key % TABLE_SIZE
#         while self.table[index] is not None and self.table[index] != 'удален':
#             index = (index + 1) % TABLE_SIZE
#         self.table[index] = key
#     def search(self, key):
#         index = key % TABLE_SIZE
#         for _ in range(TABLE_SIZE):
#             if self.table[index] is None:
#                 return False
#             if self.table[index] == key:
#                 return True
#             index = (index + 1) % TABLE_SIZE
#         return False
#     def delete(self, key):
#         index = key % TABLE_SIZE
#         for _ in range(TABLE_SIZE):
#             if self.table[index] is None:
#                 return
#             if self.table[index] == key:
#                 self.table[index] = 'удален'
#                 return
#             index = (index + 1) % TABLE_SIZE
# class Pseudo:
#     def __init__(self):
#         self.table = [None] * TABLE_SIZE
#     def _pseudo(self, key, attempt):
#         random.seed(key + attempt)
#         return random.randint(1, TABLE_SIZE - 1)
#     def insert(self, key):
#         index = key % TABLE_SIZE
#         attempt = 0
#         while self.table[index] is not None and self.table[index] != 'удален':
#             index = (index + self._pseudo(key, attempt)) % TABLE_SIZE
#             attempt += 1
#         self.table[index] = key
#     def search(self, key):
#         index = key % TABLE_SIZE
#         attempt = 0
#         for _ in range(TABLE_SIZE):
#             if self.table[index] is None:
#                 return False
#             if self.table[index] == key:
#                 return True
#             index = (index + self._pseudo(key, attempt)) % TABLE_SIZE
#             attempt += 1
#         return False
#     def delete(self, key):
#         index = key % TABLE_SIZE
#         attempt = 0
#         for _ in range(TABLE_SIZE):
#             if self.table[index] is None:
#                 return
#             if self.table[index] == key:
#                 self.table[index] = 'удален'
#                 return
#             index = (index + self._pseudo(key, attempt)) % TABLE_SIZE
#             attempt += 1
# class Chaining:
#     def __init__(self):
#         self.table = [[] for _ in range(TABLE_SIZE)]
#
#     def insert(self, key):
#         index = key % TABLE_SIZE
#         if key not in self.table[index]:
#             self.table[index].append(key)
#     def search(self, key):
#         index = key % TABLE_SIZE
#         return key in self.table[index]
#     def delete(self, key):
#         index = key % TABLE_SIZE
#         if key in self.table[index]:
#             self.table[index].remove(key)
# def generate_data(n, start=1, end=10000):
#     return random.sample(range(start, end), n)
# def test_hash_tables():
#     data = generate_data(800)
#     key = data[len(data) // 2]
#     linear = Table1()
#     pseudo = Pseudo()
#     chaining = Chaining()
#     for val in data:
#         linear.insert(val)
#         pseudo.insert(val)
#         chaining.insert(val)
#     print(f"Тест поиска элемента: {key}")
#     print("простое:", timeit.timeit(lambda: linear.search(key), number=1000))
#     print("псевдослуч:", timeit.timeit(lambda: pseudo.search(key), number=1000))
#     print("цепочки:", timeit.timeit(lambda: chaining.search(key), number=1000))
# if __name__ == "__main__":
#     test_hash_tables()



BOARD_SIZE = 8
def norm(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True
def ferz(row, board):
    if row == BOARD_SIZE:
        return board[:]
    for col in range(BOARD_SIZE):
        if norm(board, row, col):
            board[row] = col
            solution = ferz(row + 1, board)
            if solution:
                return solution
    return None
def print_board(solution):
    for row in range(BOARD_SIZE):
        line = ['.'] * BOARD_SIZE
        line[solution[row]] = 'f'
        print(' '.join(line))
if __name__ == "__main__":
    board = [-1] * BOARD_SIZE
    solution = ferz(0, board)
print_board(solution)
