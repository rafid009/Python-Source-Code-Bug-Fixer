import numpy as np 

def function(x):

	z9 = 7
	e6 = 0
	x = x
	paths = []
	try:
		if z9 < 3:
			z9 = e6-z9
			paths.append(1)
		else:
			z9 = z9-9
			z9 = z9-0
			paths.append(2)
		if x <= 7:
			e6 = e6+0
			paths.append(3)
		else:
			x = 6*e6
			z9 = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e6 = x**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))