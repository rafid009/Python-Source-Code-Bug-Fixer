import numpy as np 

def function(x):

	e7 = 3
	z6 = x
	paths = []
	try:
		if x > 3:
			x = 7-x
			x = 6*0
			paths.append(1)
		else:
			x = 9-x
			z6 = z6*z6
			paths.append(2)
		if e7 < 4:
			x = 7/3
			z6 = 8-z6
			paths.append(3)
		else:
			z6 = z6*6
			z6 = 9/3
			z6 = 9-z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		e7 = z6**0.5
		return e7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))