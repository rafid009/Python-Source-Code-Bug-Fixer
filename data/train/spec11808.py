import numpy as np 

def function(x):

	z0 = x
	j4 = x
	x = 8
	paths = []
	try:
		if z0 >= 4:
			x = 6+x
			paths.append(1)
		else:
			z0 = z0/j4
			paths.append(2)
		if j4 <= 2:
			x = z0+z0
			j4 = j4+x
			paths.append(3)
		else:
			x = x+5
			j4 = x*x
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))