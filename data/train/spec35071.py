import numpy as np 

def function(x):

	i9 = 6
	n0 = x
	paths = []
	try:
		if x > 4:
			x = 9*3
			i9 = i9*x
			x = 2/3
			paths.append(1)
		else:
			n0 = n0-i9
			paths.append(2)
		if n0 < 8:
			x = i9*x
			x = i9/2
			paths.append(3)
		else:
			n0 = n0*7
			i9 = i9/2
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		x = n0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))