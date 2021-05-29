import numpy as np 

def function(x):

	u2 = x
	e0 = x
	x = x
	paths = []
	try:
		if x <= 3:
			u2 = 7*u2
			x = e0+0
			paths.append(1)
		else:
			x = 7-x
			e0 = u2*e0
			e0 = 9-3
			paths.append(2)
		if x > 1:
			u2 = 3-x
			u2 = 0+u2
			u2 = 5-x
			paths.append(3)
		else:
			u2 = u2/8
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))