import numpy as np 

def function(x):

	k4 = 4
	l7 = x
	paths = []
	try:
		if l7 <= 3:
			x = 8*x
			paths.append(1)
		else:
			x = x*k4
			paths.append(2)
		if k4 > 9:
			l7 = l7/3
			x = 4-x
			k4 = k4+9
			paths.append(3)
		else:
			x = k4*x
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