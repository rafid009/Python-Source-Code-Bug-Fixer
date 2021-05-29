import numpy as np 

def function(x):

	u0 = x
	l6 = 1
	x = x
	paths = []
	try:
		if x > 6:
			u0 = u0+8
			u0 = 4/l6
			paths.append(1)
		else:
			x = x-6
			l6 = l6-8
			paths.append(2)
		if x >= 1:
			u0 = 9+2
			paths.append(3)
		else:
			u0 = 5/x
			l6 = x/l6
			paths.append(4)
		paths.append(5)
		assert u0 >= 0
		x = u0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))