import numpy as np 

def function(x):

	a9 = 8
	i0 = 7
	paths = []
	try:
		if x > 0:
			a9 = a9+7
			a9 = 6*x
			i0 = i0-0
			paths.append(1)
		else:
			x = 5+x
			paths.append(2)
		if x < 4:
			a9 = 6/1
			paths.append(3)
		else:
			a9 = 4+3
			i0 = i0-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a9 = x**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))