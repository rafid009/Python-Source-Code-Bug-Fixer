import numpy as np 

def function(x):

	e3 = x
	k5 = 8
	paths = []
	try:
		if e3 < 5:
			e3 = e3/6
			k5 = 6+6
			paths.append(1)
		else:
			x = 2-x
			k5 = 1/2
			e3 = 9-6
			paths.append(2)
		if e3 > 9:
			k5 = 5*k5
			x = k5+x
			paths.append(3)
		else:
			e3 = 5-5
			e3 = 4-1
			k5 = k5*k5
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