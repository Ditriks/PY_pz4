# Вычислить число c заданной точностью d

# from math import pi
# d = input()
# accu = len(d)
# print(str(pi)[0:accu])



# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# n = int(input())
# if n == 1:
#     print(1)
# new_list = []
# for i in range(1, n // 2 + 1):
#     if n % i == 0:
#         for j in range(2, i //2 + 1):
#             if i % j ==0:
#                 break
#         else:
#             new_list.append(i)
# print(*new_list, sep=', ')



# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

f_list = [int(i) for i in input().split()]
for i in f_list:
   if f_list.count(i) == 1:
       print(i)