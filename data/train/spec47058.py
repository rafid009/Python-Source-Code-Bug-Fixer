import numpy as np 

def function(x):

	z4 = 3
	q7 = 2
	paths = []
	try:
		if x <= 1:
			x = x*4
			paths.append(1)
		else:
			z4 = 5-1
			x = x+5
			x = 5-x
			paths.append(2)
		if z4 >= 4:
			z4 = z4/5
			paths.append(3)
		else:
			x = x-5
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