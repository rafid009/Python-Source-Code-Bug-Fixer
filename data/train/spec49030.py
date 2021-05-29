import numpy as np 

def function(x):

	l0 = x
	u3 = 7
	paths = []
	try:
		if x >= 5:
			x = 4+x
			x = 3/x
			paths.append(1)
		else:
			l0 = 0*x
			paths.append(2)
		if x < 0:
			x = 8*x
			u3 = 4-u3
			l0 = x-l0
			paths.append(3)
		else:
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u3 = x**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))