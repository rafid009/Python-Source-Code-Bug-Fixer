import numpy as np 

def function(x):

	j7 = 1
	y1 = 4
	paths = []
	try:
		if y1 >= 9:
			x = 5*x
			j7 = x+0
			j7 = y1-j7
			paths.append(1)
		else:
			j7 = 2-4
			j7 = 9*j7
			j7 = 6/j7
			paths.append(2)
		if x >= 6:
			j7 = 8/7
			j7 = j7*j7
			y1 = y1-y1
			paths.append(3)
		else:
			x = x+y1
			y1 = j7+j7
			y1 = y1/7
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		x = j7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))