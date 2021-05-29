import numpy as np 

def function(x):

	i9 = x
	a7 = 6
	paths = []
	try:
		if a7 > 1:
			x = x*x
			a7 = a7-7
			paths.append(1)
		else:
			i9 = i9*4
			x = 4*x
			paths.append(2)
		if x <= 6:
			x = 4-x
			paths.append(3)
		else:
			i9 = 9-i9
			i9 = x/8
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