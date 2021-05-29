import numpy as np 

def function(x):

	z2 = 6
	y5 = x
	paths = []
	try:
		if z2 <= 4:
			z2 = z2-y5
			paths.append(1)
		else:
			z2 = 4/x
			y5 = 0+y5
			paths.append(2)
		if y5 <= 1:
			z2 = 3*y5
			y5 = y5-2
			paths.append(3)
		else:
			x = z2*3
			z2 = z2/8
			y5 = y5/6
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		y5 = z2**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))