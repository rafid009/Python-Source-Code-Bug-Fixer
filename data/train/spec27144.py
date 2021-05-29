import numpy as np 

def function(x):

	y0 = x
	z2 = x
	x = 3
	paths = []
	try:
		if x > 9:
			x = 1+7
			x = 0-x
			paths.append(1)
		else:
			x = x-6
			paths.append(2)
		if z2 <= 2:
			y0 = 1+y0
			paths.append(3)
		else:
			z2 = z2*2
			x = 3-x
			x = x+1
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		y0 = z2**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))