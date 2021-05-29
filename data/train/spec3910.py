import numpy as np 

def function(x):

	d7 = 6
	u1 = x
	paths = []
	try:
		if u1 > 0:
			x = x*x
			paths.append(1)
		else:
			x = x-x
			paths.append(2)
		if u1 <= 2:
			x = 4+u1
			u1 = 3*u1
			paths.append(3)
		else:
			u1 = 0-9
			x = x/5
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