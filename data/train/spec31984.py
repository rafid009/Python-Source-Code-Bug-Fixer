import numpy as np 

def function(x):

	x1 = 4
	e8 = x
	x = 3
	paths = []
	try:
		if x1 <= 9:
			e8 = e8-8
			e8 = x1*e8
			paths.append(1)
		else:
			e8 = x1/3
			e8 = 3/4
			paths.append(2)
		if x >= 8:
			x1 = 1-9
			paths.append(3)
		else:
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x1 = e8**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))