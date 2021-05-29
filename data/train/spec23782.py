import numpy as np 

def function(x):

	x9 = 4
	j7 = x
	paths = []
	try:
		if j7 >= 5:
			j7 = 6+3
			x9 = x9/7
			paths.append(1)
		else:
			x9 = x9*x9
			x9 = 9-x9
			paths.append(2)
		if j7 > 5:
			x = j7/7
			paths.append(3)
		else:
			x = 2/x
			x9 = x9-x
			x9 = x9*1
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