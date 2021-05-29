import numpy as np 

def function(x):

	a0 = 8
	w7 = x
	paths = []
	try:
		if x < 3:
			a0 = x*w7
			a0 = x*a0
			paths.append(1)
		else:
			x = a0+0
			paths.append(2)
		if a0 > 3:
			a0 = a0/a0
			paths.append(3)
		else:
			a0 = 1*a0
			a0 = a0+w7
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