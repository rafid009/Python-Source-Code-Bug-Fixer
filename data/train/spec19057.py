import numpy as np 

def function(x):

	e7 = 2
	z9 = 6
	paths = []
	try:
		if e7 >= 3:
			x = 5-e7
			z9 = z9*1
			paths.append(1)
		else:
			x = x*3
			x = x/7
			e7 = z9/e7
			paths.append(2)
		if z9 < 7:
			z9 = z9+9
			e7 = 0/z9
			z9 = e7-x
			paths.append(3)
		else:
			x = x-z9
			e7 = 3-7
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