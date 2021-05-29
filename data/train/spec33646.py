import numpy as np 

def function(x):

	e9 = x
	y7 = x
	paths = []
	try:
		if x <= 9:
			x = x*x
			x = e9-3
			e9 = e9/4
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x < 3:
			x = x/9
			x = 7+3
			e9 = 5*5
			paths.append(3)
		else:
			e9 = e9*e9
			e9 = 7-e9
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))