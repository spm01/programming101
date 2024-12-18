# -*- coding: utf-8 -*-
"""113Z29044_HW2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10dDJ1Scnw0zIVzypfhvtAtrsn04u0hy1
"""

#[dictionary] Write a program to create a dictionary.
#If use enter an integer (n), the dictionary is (key,value)=(i, i*i).
#Input: 8
#Output: print the dictionary= {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

dict1 = {}
n = int(input("Enter a whole number: "))
for i in range(1, n+1):
  dict1[i] = i * i
print(dict1)

#[What’s my acronym] Ask the user to enter the full meaning of an organization or
#concept and you'll provide the acronym to the user.
#For example:
#Input: As soon as possible. Output: ASAP
#Input: World health organization. Output: WHO
#Input: absent without leave. Output: AWL

user_input = input("Input a string of words: ")
words = user_input.split()
acronym = []

for word in words:
  first_letter = word[0].upper()
  acronym.append(first_letter)

result = "".join(acronym)
print(result)

#[Count and say] The count-and-say sequence is a equence of digit strings.For
#example: Input(digit strings):”3322251”, output:”23321511” (see the following figure)
n = int(input("Input a number! "))
def count_and_say(n: int) -> str:
  """
  1
  11
  21
  1211
  111221
  312211
  """
  if n == 1:
    return "1"

  prev = count_and_say(n-1)
  res = ""
  count = 1

  for i in range(len(prev)):
    if i ==len(prev)-1 or prev[i] != prev[i+1]:
      res += str(count) + prev[i]
      count = 1
    else:
      count += 1

  return res
count_and_say(n)

#[Single number] Design a program that asks the user to enter a series of 5
#numbers using loop statement stored in a list nums, every element appears twice
#except for one. Find that single one. For example,
#Input:nums=[4,1,2,1,2], output=4
#Input: nums=[1,3,7,1,3], output=7

nums = list(input("Enter a series of 5 numbers: "))

def single_count(nums):
  for num in nums:
    if nums.count(num) == 1:
      return num
  return None
result = single_count(nums)
print(result)

#[list] Design a program that asks the user to enter a series of 10 numbers. The
#program should store the numbers in a list list_num and then display the
#following data:
#The lowest number in the list
#The highest number in the list
#The total of the numbers in the list
#The average of the numbers in the list

from decimal import Decimal
import statistics

user_input = list(input("Enter a series of 10 numbers: "))

def ten_numbers():
    low = min(Decimal(i) for i in user_input)
    high = max(Decimal(i) for i in user_input)
    total = sum(Decimal(i) for i in user_input)
    avg = statistics.mean(Decimal(i) for i in user_input)
    print(low, high, total, avg)
ten_numbers()