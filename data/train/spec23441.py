import numpy as np 

def function(x):

	z1 = 9
	y8 = x
	x = 0
	paths = []
	try:
		if z1 <= 1:
			x = 1+x
			paths.append(1)
		else:
			z1 = 1/1
			y8 = 2*y8
			y8 = y8+5
			paths.append(2)
		if z1 <= 6:
			y8 = y8+3
			x = x*x
			y8 = y8+6
			paths.append(3)
		else:
			z1 = z1/4
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))