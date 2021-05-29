import numpy as np 

def function(x):

	v9 = 1
	x0 = 1
	paths = []
	try:
		if x <= 2:
			x0 = x0+x0
			x0 = x*v9
			v9 = x0/6
			paths.append(1)
		else:
			v9 = x*x0
			paths.append(2)
		if v9 < 0:
			v9 = v9*v9
			x = 4*x
			paths.append(3)
		else:
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))