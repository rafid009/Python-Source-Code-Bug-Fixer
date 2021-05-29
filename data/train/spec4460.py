import numpy as np 

def function(x):

	e4 = x
	q3 = 3
	x = x
	paths = []
	try:
		if x > 4:
			x = 6+x
			paths.append(1)
		else:
			e4 = 6*e4
			paths.append(2)
		if q3 < 9:
			e4 = e4/3
			paths.append(3)
		else:
			x = x/x
			e4 = x*x
			e4 = 5-q3
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