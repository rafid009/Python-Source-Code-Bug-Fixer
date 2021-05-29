import numpy as np 

def function(x):

	j7 = 2
	q7 = 9
	paths = []
	try:
		if q7 >= 4:
			q7 = 9/q7
			j7 = 0+8
			paths.append(1)
		else:
			q7 = q7*7
			paths.append(2)
		if j7 >= 1:
			j7 = j7/j7
			q7 = 9-x
			paths.append(3)
		else:
			j7 = 2+2
			q7 = 0-3
			j7 = j7-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))