import numpy as np 

def function(x):

	z6 = x
	e2 = 3
	paths = []
	try:
		if z6 <= 3:
			z6 = x/1
			paths.append(1)
		else:
			x = x+6
			x = 4+x
			z6 = e2*z6
			paths.append(2)
		if x >= 1:
			e2 = 9*e2
			paths.append(3)
		else:
			e2 = 6+x
			z6 = z6/8
			e2 = z6/3
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		e2 = z6**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))