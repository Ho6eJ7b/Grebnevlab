# from collections import deque
# with open('knigi.txt') as file:
#     lines = file.readlines()
# deq1 = deque()
# deq2 = deque()
# for line in lines:
#     deq1.append(line.strip())
# while deq1:
#     smallest = min(deq1)
#     deq1.remove(smallest)
#     deq2.append(smallest)
#     print(smallest)


# from collections import deque
# deq = deque(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
# with open('shifr.txt') as file:
#     shifr = file.read()
# neshifr = ''
# for char in shifr:
#     if char.isalpha():
#         index = deq.index(char)
#         decrypted_char = deq[(index - 1) % len(deq)]
#         neshifr += decrypted_char
#     else:
#         neshifr += char
# print(neshifr)


# def move(source, target, source_name, target_name):
#     disk = source.pop()
#     target.append(disk)
#     output = f" {disk} с {source_name}: {source} на {target_name}: {target}"
#     print(output)
# def bashnya(n, source, target, auxiliary, source_name, target_name, auxiliary_name):
#     if n == 1:
#         move(source, target, source_name, target_name)
#         return
#     bashnya(n-1, source, auxiliary, target, source_name, auxiliary_name, target_name)
#     move(source, target, source_name, target_name)
#     bashnya(n-1, auxiliary, target, source, auxiliary_name, target_name, source_name)
# with open('diski.txt', 'r') as file:
#     disks = [int(line.strip()) for line in file]
# stack_a = disks[::-1]  
# stack_b = [] 
# stack_c = []
# bashnya(len(disks), stack_a, stack_c, stack_b, 'A', 'C', 'B')


# def check_brackets_balance(file_path):
#     stack = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             for char in line:
#                 if char == '(':
#                     stack.append('(')
#                 elif char == ')':
#                     if not stack:
#                         return False
#                     stack.pop()
#     return len(stack) == 0
# file_path = 'proga.txt'
# if check_brackets_balance(file_path):
#     print("баланс))")
# else:
#     print("не баланс(")


# from collections import deque
# def check_brackets_balance(file_name):
#     stack = deque()
#     with open(file_name, 'r') as file:
#         for line in file:
#             for char in line:
#                 if char == '[':
#                     stack.append('[')
#                 elif char == ']':
#                     if not stack:
#                         return False
#                     stack.pop()
#     return len(stack) == 0
# file_name = 'progaa.txt'
# if check_brackets_balance(file_name):
#     print("баланс))")
# else:
#     print("не баланс(")


# def print_characters_by_type(file_name):
#     characters = []
#     with open(file_name) as file:
#         for line in file:
#             for char in line:
#                 characters.append(char)
#     cifri = []
#     bukvi = []
#     ostatok = []
#     for char in characters:
#         if char.isdigit():
#             cifri.append(char)
#         elif char.isalpha():
#             bukvi.append(char)
#         else:
#             ostatok.append(char)
#     print("Цифры:")
#     for char in characters:
#         if char in cifri:
#             print(char, end='')
#     print("\nБуквы:")
#     for char in characters:
#         if char in bukvi:
#             print(char, end='')
#     print("\nОстальные символы:")
#     for char in characters:
#         if char in ostatok:
#             print(char, end='')
# file_name = 'file123.txt'
# print_characters_by_type(file_name)


# from collections import deque
# def print_numbers_by_sign(file_name):
#     negativ = deque()
#     positiv = deque()
#     with open(file_name) as file:
#         for line in file:
#             numbers = map(int, line.split())
#             for num in numbers:
#                 if num < 0:
#                     negativ.append(num)
#                 else:
#                     positiv.append(num)
#     print("минусы")
#     while negativ:
#         neg_num = negativ.popleft()
#         print(neg_num)
#     print("плюсы")
#     while positiv:
#         pos_num = positiv.popleft()
#         print(pos_num)
# file_name = 'chisla.txt'
# print_numbers_by_sign(file_name)


# def reverse_file(input_file, output_file):
#     stack = []
#     with open(input_file, 'r') as file:
#         for line in file:
#             stack.append(line.strip())
#     with open(output_file, 'w') as out_file:
#         while stack:
#             line = stack.pop()
#             print(line) 
#             out_file.write(f"{line}\n")
# input_file = 'stroki.txt'
# output_file = 'obrstroki.txt'
# reverse_file(input_file, output_file)
