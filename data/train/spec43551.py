import numpy as np 

def function(x):

	d5 = x
	j0 = 4
	paths = []
	try:
		if j0 < 6:
			j0 = j0+7
			paths.append(1)
		else:
			j0 = x-9
			j0 = j0/j0
			paths.append(2)
		if x > 0:
			x = x*j0
			d5 = 4+d5
			paths.append(3)
		else:
			x = x+3
			j0 = j0+4
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