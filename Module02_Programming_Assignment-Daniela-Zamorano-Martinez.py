"""

Author:  Daniela Zamorano-Martinez
Date written: 11/01/24
Assignment:   Module02 Programming Assignment part1 
Short Desc:   Letting user enter 2 primary colors to mix them.


"""
#Define the colors in the array
primary_colors = {"red", "blue", "yellow"}

#recieve input from user
color_1 = input("Enter the first primary color: ")
color_2 = input("Enter the second primary color: ")

#If-condition to make sure user only enters primary colors
if color_1 not in primary_colors or color_2 not in primary_colors:
    print("Error! Please enter a primary color.")
#if-condition to make sure user mixes two different primary colors
elif color_1 == color_2:
    print("Error! Please enter a different primary color.")
else:
    #if section to avoid long coding
    #outputs the results of mixing primary colors
    if (color_1 == "red" and color_2 == "blue") or (color_1 == "blue" and color_2 == "red"):
        print("The result of mixing red and blue is purple.")
    elif (color_1 == "red" and color_2 == "yellow") or (color_1 == "yellow" and color_2 == "red"):
        print("The result of mixing red and yellow is orange.")
    elif (color_1 == "yellow" and color_2 == "blue") or (color_1 == "blue" and color_2 == "yellow"):
        print("The result of mixing yellow and blue is green.")