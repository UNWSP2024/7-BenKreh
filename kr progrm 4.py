#Ben Krehbiel
#3/7/2025
#mathematician

import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

def mathematician():

    while True:
        try:
            x1 = float(input("Enter first x cord "))
            y1 = float(input("Enter first y cord "))
            z1 = float(input("Enter first z cord "))
            p1 = (x1, y1, z1)  

            x2 = float(input("Enter second x cord: "))
            y2 = float(input("Enter second y cord: "))
            z2 = float(input("Enter second z cord: "))
            p2 = (x2, y2, z2)  

            result = distance(p1, p2)
            print(f"\nThe distance between {p1} and {p2} is: {result:.2f}")
            break  

        except ValueError:
            print("Invalid input")


mathematician()
