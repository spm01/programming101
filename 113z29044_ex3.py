# -*- coding: utf-8 -*-
"""113Z29044_ex3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Qw201I-XAxBS3t3cSvdELwtk_dfH4fVh
"""

#Q1
weight = float(input('weight:'))
height = float(input('height:'))

BMI = weight / (height / 100)**2
print(BMI)

if BMI <= 18.5:
    print('underwieght BMI')
elif BMI <= 24:
    print('normal BMI')
elif BMI <= 27:
    print('overweight BMI')
else:
    print('obese')

#Q2
speed = float(input('speed:'))

if 24<speed<56:
    print('Speed is normal')
else:
    print('Speed is abnormal')

#Q3
books = float(input('Number of books bought:'))
if books >= 4:
    points = 60
elif books == 3:
    points = 30
elif books == 2:
    points = 15
elif books == 1:
    points = 5
else:
    points = 0
print("Points Earned:", points)