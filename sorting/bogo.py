# Python program for implementation of Bogo Sort
import random


# Sorts array a[0..n-1] using Bogo sort


def bogoSort(a):
    n = len(a)
    while (is_sorted(a) == False):
        shuffle(a)

    # To check if array is sorted or not


def is_sorted(a):
    n = len(a)
    for i in range(0, n - 1):
        if (a[i] > a[i + 1]):
            return False
    return True


# To generate permutation of the array


def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        a[i], a[r] = a[r], a[i]

    # Driver code to test above


a = [23, 65 ,87, 98, 10, 23, 84, 63, 81, 90]
bogoSort(a)
print("Sorted array :")
for i in range(len(a)):
    print("%d" % a[i]),