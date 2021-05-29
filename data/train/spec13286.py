import numpy as np 

def function(x):

	e5 = x
	z1 = x
	paths = []
	try:
		if e5 <= 8:
			e5 = e5-1
			z1 = 1*z1
			z1 = z1*x
			paths.append(1)
		else:
			e5 = e5-2
			x = x+e5
			paths.append(2)
		if x >= 5:
			z1 = 5/3
			paths.append(3)
		else:
			z1 = x/8
			paths.append(4)
		paths.append(5)
		assert z1 >= 0
		e5 = z1**0.5
		return e5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))