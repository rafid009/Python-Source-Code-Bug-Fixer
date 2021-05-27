import numpy as np 

def function(x):

	i4 = 8
	a9 = 7
	paths = []
	try:
		if a9 < 9:
			a9 = a9-a9
			paths.append(1)
		else:
			a9 = a9/6
			paths.append(2)
		if a9 <= 9:
			a9 = a9+6
			x = x+0
			paths.append(3)
		else:
			x = i4*x
			x = i4*x
			a9 = 8-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))