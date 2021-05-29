import numpy as np 

def function(x):

	i7 = 5
	z1 = 5
	paths = []
	try:
		if i7 < 1:
			x = z1-x
			z1 = i7-x
			paths.append(1)
		else:
			z1 = z1/8
			paths.append(2)
		if z1 >= 2:
			z1 = 7+z1
			x = x/6
			x = z1+z1
			paths.append(3)
		else:
			x = 5+x
			z1 = x+i7
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		x = z1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))