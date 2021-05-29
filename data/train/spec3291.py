import numpy as np 

def function(x):

	z2 = 9
	y7 = x
	paths = []
	try:
		if z2 < 4:
			x = x+3
			x = 6+x
			paths.append(1)
		else:
			x = y7-8
			paths.append(2)
		if z2 >= 6:
			y7 = 5/8
			y7 = z2-1
			paths.append(3)
		else:
			z2 = z2*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))