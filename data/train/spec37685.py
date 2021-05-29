import numpy as np 

def function(x):

	b4 = 6
	z4 = 6
	paths = []
	try:
		if z4 >= 9:
			z4 = 9*1
			x = 1-x
			x = x+x
			paths.append(1)
		else:
			b4 = z4/3
			z4 = 9/z4
			paths.append(2)
		if z4 < 7:
			b4 = 2+b4
			paths.append(3)
		else:
			b4 = 6*3
			x = x-0
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