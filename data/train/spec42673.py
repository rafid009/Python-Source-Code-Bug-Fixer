import numpy as np 

def function(x):

	a5 = x
	z6 = 0
	paths = []
	try:
		if a5 > 5:
			a5 = 8-2
			paths.append(1)
		else:
			z6 = z6+3
			x = z6/x
			z6 = a5+8
			paths.append(2)
		if z6 >= 1:
			a5 = a5*3
			z6 = x*x
			paths.append(3)
		else:
			x = x+4
			a5 = x+a5
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		x = a5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))