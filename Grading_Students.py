#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    newgrade=[]
    for grade in grades:
        # Write your code here
        assert 0<=grade<=100,"the grade: 0<=grade<=100"
        difference=grade%5
        if grade<38 or difference<3:
            newgrade.append(grade)
        else:
            newgrade.append(grade-difference+5)
    return newgrade

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
