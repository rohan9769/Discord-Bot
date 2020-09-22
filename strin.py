# Q2  - How do you find the second highest number in an integer array? (Without Using in built function).
# lst = [5,3,1,8,9]
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         temp = lst[i]
#         lst[i] = lst[j]
#         lst[j] = temp
# print(f'Second largest number is {lst[1]}')

# Q1 - Anagram
# def detectAnangram(s1,s2):
#     # print(list(s1))
#     # print(list(s2))
#     for i in range(len(list(s1))):
#         for j in range(len(list(s2))):
#            if s1[i] == s2[j] and len(s1)==len(s2):
#                print('Anagram')
#                break
#
# detectAnangram('Mary','Army')


# Q3 - Pattern
# n=int(input('Enter a number : '))
# for i in range(1,2):
#     print(' ')
#     for j in range(1,n):
#         print('*'*j)
#     for k in range(n,0,-1):
#         print('*'*k)

# Q4 - Given a string, print the repeated characters if they are consecutive till a different character is detected (print from second consecutive repetative character till non repetative charcater is detected) with their position index.
# Example. Input - Helllol or Assasssin
# Output - llo at position 3,4,5 or sa at position 2,3 and ssi at position 5,6,7
# str = input('Enter the string : ')
# subs = []
# for i in range(len(str)-1):
#     if str[i] == str[i+1]:
#         print(str[i])
#         print(str[i+1])


import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# # game loop
#
# while True:
#     max = 0
#     maxIndex = -1
#     for i in range(8):
#         mountain_h = int(input())  # represents the height of one mountain.
#         if mountain_h > max:
#             max = mountain_h
#             maxIndex = i
#         # if(max(mountain_h)<mountain_h):
#         #     max(mountain_h) = mountain_h
#         #     max(mountain_h)  = i
#     # Write an action using print
#     # To debug: print("Debug messages...", file=sys.stderr, flush=True)
#
#     # The index of the mountain to fire on.
#     print(maxIndex)
#






