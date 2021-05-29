import numpy as np 

def function(x):

	j0 = x
	z0 = 2
	paths = []
	try:
		if j0 > 0:
			x = x*2
			x = z0*x
			j0 = z0-z0
			paths.append(1)
		else:
			x = 9*8
			x = 3/j0
			paths.append(2)
		if z0 <= 7:
			x = 3*j0
			paths.append(3)
		else:
			z0 = 4-z0
			x = x-7
			z0 = 2*8
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))