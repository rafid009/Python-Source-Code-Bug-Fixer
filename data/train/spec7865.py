import numpy as np 

def function(x):

	z6 = 1
	j1 = 6
	paths = []
	try:
		if z6 > 5:
			j1 = j1/5
			z6 = z6-0
			paths.append(1)
		else:
			z6 = 7-z6
			paths.append(2)
		if z6 > 7:
			z6 = 8-x
			j1 = 1/j1
			x = z6/8
			paths.append(3)
		else:
			z6 = 4+x
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))