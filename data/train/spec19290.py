import numpy as np 

def function(x):

	z6 = 9
	e5 = x
	paths = []
	try:
		if e5 >= 8:
			x = z6/x
			z6 = z6/1
			e5 = e5-1
			paths.append(1)
		else:
			e5 = 9/e5
			paths.append(2)
		if x < 2:
			z6 = 5*e5
			e5 = e5-2
			e5 = e5*e5
			paths.append(3)
		else:
			e5 = 5+e5
			x = z6+e5
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))