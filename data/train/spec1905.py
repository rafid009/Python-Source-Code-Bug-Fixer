import numpy as np 

def function(x):

	u3 = x
	a5 = x
	paths = []
	try:
		if x > 6:
			x = x-9
			paths.append(1)
		else:
			u3 = 4*u3
			x = 9/6
			paths.append(2)
		if x <= 1:
			u3 = 6*u3
			a5 = 8+a5
			paths.append(3)
		else:
			a5 = a5*x
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