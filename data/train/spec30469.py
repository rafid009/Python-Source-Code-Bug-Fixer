import numpy as np 

def function(x):

	z6 = x
	i0 = x
	paths = []
	try:
		if i0 >= 4:
			i0 = 3+z6
			paths.append(1)
		else:
			z6 = z6*0
			x = x+3
			paths.append(2)
		if z6 >= 0:
			z6 = z6+4
			z6 = 7/7
			paths.append(3)
		else:
			i0 = x+i0
			z6 = i0+z6
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		z6 = i0**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))