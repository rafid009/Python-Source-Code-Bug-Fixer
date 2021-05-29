import numpy as np 

def function(x):

	k7 = x
	e5 = x
	paths = []
	try:
		if x <= 5:
			e5 = e5*2
			x = 1-3
			paths.append(1)
		else:
			k7 = 8+e5
			e5 = 6*e5
			k7 = 6-k7
			paths.append(2)
		if e5 < 8:
			x = 1-x
			paths.append(3)
		else:
			e5 = e5*6
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