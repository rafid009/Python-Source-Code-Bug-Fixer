import numpy as np 

def function(x):

	i0 = x
	z8 = x
	paths = []
	try:
		if z8 <= 3:
			i0 = z8+5
			paths.append(1)
		else:
			z8 = 0/4
			paths.append(2)
		if x < 1:
			z8 = z8+z8
			paths.append(3)
		else:
			z8 = 5*0
			i0 = 0-i0
			z8 = z8-0
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		i0 = z8**0.5
		return i0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))