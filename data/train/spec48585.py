import numpy as np 

def function(x):

	e5 = x
	u4 = x
	x = x
	paths = []
	try:
		if e5 > 0:
			u4 = 1-e5
			paths.append(1)
		else:
			u4 = u4+e5
			e5 = e5*7
			paths.append(2)
		if x > 2:
			x = x+1
			paths.append(3)
		else:
			e5 = x-e5
			e5 = 3+e5
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