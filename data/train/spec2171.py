import numpy as np 

def function(x):

	e9 = 9
	x3 = x
	paths = []
	try:
		if x3 <= 9:
			x3 = x/7
			e9 = 1-8
			paths.append(1)
		else:
			x = x+8
			x = 3-x
			paths.append(2)
		if e9 >= 8:
			x = 6-x
			paths.append(3)
		else:
			x3 = x3/x3
			x3 = 4-e9
			x3 = 7+x3
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