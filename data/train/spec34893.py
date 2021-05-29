import numpy as np 

def function(x):

	a8 = x
	u3 = x
	paths = []
	try:
		if u3 < 0:
			a8 = 7+a8
			paths.append(1)
		else:
			a8 = a8+0
			paths.append(2)
		if x < 3:
			a8 = u3+0
			paths.append(3)
		else:
			a8 = 9*8
			x = 7-x
			a8 = 1/a8
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