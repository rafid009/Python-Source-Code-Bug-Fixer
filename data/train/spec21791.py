import numpy as np 

def function(x):

	j0 = x
	o7 = 2
	x = 1
	paths = []
	try:
		if j0 >= 6:
			j0 = 7+j0
			paths.append(1)
		else:
			j0 = j0/j0
			j0 = j0*5
			paths.append(2)
		if x >= 0:
			x = x*2
			j0 = o7*5
			x = o7-3
			paths.append(3)
		else:
			j0 = o7-j0
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