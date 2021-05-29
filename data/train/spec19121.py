import numpy as np 

def function(x):

	i0 = 5
	x1 = 0
	paths = []
	try:
		if x <= 4:
			x1 = i0*2
			paths.append(1)
		else:
			x = x/i0
			i0 = 6/i0
			paths.append(2)
		if x1 < 4:
			x = 0+2
			x = x1+5
			paths.append(3)
		else:
			x = 3*x
			x = x-x1
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