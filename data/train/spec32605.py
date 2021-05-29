import numpy as np 

def function(x):

	e5 = 2
	z7 = 9
	paths = []
	try:
		if x <= 6:
			x = x/4
			paths.append(1)
		else:
			z7 = z7*x
			paths.append(2)
		if e5 >= 7:
			z7 = 4*x
			paths.append(3)
		else:
			e5 = 6+e5
			z7 = e5*x
			e5 = e5-9
			paths.append(4)
		paths.append(5)
		assert z7 >= 0
		x = z7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))