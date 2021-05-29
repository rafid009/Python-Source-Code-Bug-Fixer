import numpy as np 

def function(x):

	e7 = x
	n8 = 4
	paths = []
	try:
		if x >= 3:
			e7 = x+5
			x = x-6
			paths.append(1)
		else:
			n8 = n8/6
			e7 = 3/e7
			paths.append(2)
		if n8 <= 9:
			e7 = 1-e7
			paths.append(3)
		else:
			n8 = n8/8
			n8 = n8-n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))