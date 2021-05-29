import numpy as np 

def function(x):

	q8 = x
	x7 = 0
	paths = []
	try:
		if x <= 5:
			x7 = 7-x7
			x7 = 4-x7
			x = x+6
			paths.append(1)
		else:
			q8 = q8*5
			paths.append(2)
		if x <= 4:
			x = x+0
			x = x7-1
			x = q8-x
			paths.append(3)
		else:
			x7 = x7+q8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))