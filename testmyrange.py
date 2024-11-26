"""
Author: Daniela Zamorano-Martinez
Date: 11/25/24
Assignment: Module 5 Practice Exercise 6-6
Returns as a list with a specific number range. 

"""

def myRange(start, stop= None, step =1):
#Starting the range
	if stop is None:
		stop=start
		start = 0
#Stopping the vaule
	if step ==0:
		raise ValueError("Step can not be zero!")
	
	result = []
#incrementration 
	if step>0:
		while start< stop:
			result.append(start)
			start += step
	else:
		while start > stop:
			result.append (start)
			start += step

#returns the numbers in specified range
	return result

if __name__ == "__main__":
	print(myRange(9))
	print(myRange(0))
	print(myRange(20))
	print(myRange(-5))