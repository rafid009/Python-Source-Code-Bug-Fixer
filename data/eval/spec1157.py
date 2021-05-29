import numpy as np 

def function(x):

	e7 = x
	r2 = 7
	paths = []
	try:
		if x >= 0:
			e7 = e7*6
			e7 = 7*x
			paths.append(1)
		else:
			e7 = e7-8
			r2 = x+r2
			paths.append(2)
		if r2 <= 8:
			e7 = 9+e7
			paths.append(3)
		else:
			e7 = e7-x
			r2 = r2/3
			r2 = 5-7
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