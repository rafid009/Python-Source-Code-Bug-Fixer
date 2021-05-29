import numpy as np 

def function(x):

	e8 = 7
	k6 = x
	paths = []
	try:
		if e8 >= 1:
			e8 = 1/x
			paths.append(1)
		else:
			e8 = e8-7
			e8 = e8/2
			paths.append(2)
		if k6 < 8:
			e8 = 1*3
			paths.append(3)
		else:
			k6 = k6-7
			e8 = 6*x
			x = x/k6
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