import numpy as np 

def function(x):

	j3 = 1
	z0 = 6
	paths = []
	try:
		if z0 <= 3:
			z0 = 0*1
			paths.append(1)
		else:
			z0 = z0-x
			x = 2-x
			j3 = j3/1
			paths.append(2)
		if x < 2:
			j3 = 2/x
			x = 8-9
			z0 = x/7
			paths.append(3)
		else:
			z0 = z0-2
			j3 = 4/j3
			j3 = 5+j3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))