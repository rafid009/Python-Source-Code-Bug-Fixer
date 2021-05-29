import numpy as np 

def function(x):

	i0 = x
	z1 = x
	paths = []
	try:
		if i0 < 3:
			z1 = i0/4
			x = x*6
			paths.append(1)
		else:
			z1 = 9*6
			x = 3+i0
			paths.append(2)
		if i0 > 0:
			z1 = z1+8
			x = 4/x
			x = x+i0
			paths.append(3)
		else:
			z1 = z1+z1
			x = 8+1
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