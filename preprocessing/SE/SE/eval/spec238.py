import numpy as np 

def function(x):

	j1 = 6
	z0 = 4
	paths = []
	try:
		if j1 <= 8:
			j1 = j1+8
			z0 = j1*x
			paths.append(1)
		else:
			j1 = j1*z0
			paths.append(2)
		if x > 2:
			x = 7*j1
			paths.append(3)
		else:
			z0 = j1-z0
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))