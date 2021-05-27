import numpy as np 

def function(x):

	f7 = x
	u2 = 2
	paths = []
	try:
		if f7 > 3:
			f7 = f7-x
			x = x*x
			x = 5/x
			paths.append(1)
		else:
			u2 = 4*u2
			u2 = 1-3
			paths.append(2)
		if f7 > 1:
			f7 = 8+f7
			paths.append(3)
		else:
			x = f7*2
			x = 2*f7
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