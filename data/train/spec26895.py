import numpy as np 

def function(x):

	z4 = 9
	f7 = 5
	paths = []
	try:
		if z4 >= 6:
			x = x+6
			z4 = x+2
			paths.append(1)
		else:
			f7 = 0+f7
			x = 0+z4
			paths.append(2)
		if x < 1:
			x = x*9
			paths.append(3)
		else:
			x = z4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))