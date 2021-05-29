import numpy as np 

def function(x):

	z6 = x
	e1 = 4
	paths = []
	try:
		if z6 >= 3:
			e1 = z6+1
			e1 = e1/5
			x = 9-x
			paths.append(1)
		else:
			e1 = z6*e1
			e1 = 1*x
			paths.append(2)
		if z6 > 1:
			z6 = 6/2
			x = x+7
			paths.append(3)
		else:
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		e1 = z6**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))