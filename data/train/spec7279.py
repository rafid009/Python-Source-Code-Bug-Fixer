import numpy as np 

def function(x):

	z4 = 6
	x2 = 1
	paths = []
	try:
		if z4 >= 4:
			z4 = z4-3
			paths.append(1)
		else:
			z4 = 6-3
			x2 = x2*3
			paths.append(2)
		if z4 <= 4:
			x2 = x2+9
			x2 = x*x2
			x = x-1
			paths.append(3)
		else:
			x2 = x2*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z4 = x**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))