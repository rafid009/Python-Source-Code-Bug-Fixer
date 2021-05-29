import numpy as np 

def function(x):

	a7 = x
	x7 = x
	x = 6
	paths = []
	try:
		if a7 <= 8:
			x7 = 4+x7
			x7 = 9/8
			paths.append(1)
		else:
			x7 = x-x7
			x7 = x7*x7
			paths.append(2)
		if x < 9:
			x = 5+x
			x7 = a7/x7
			a7 = a7/5
			paths.append(3)
		else:
			x = 1-x
			x = x/9
			x = x-4
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x = x7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))