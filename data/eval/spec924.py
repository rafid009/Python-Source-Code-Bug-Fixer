import numpy as np 

def function(x):

	l4 = x
	z4 = 7
	paths = []
	try:
		if l4 >= 7:
			x = 5*z4
			x = 7-1
			l4 = 1-l4
			paths.append(1)
		else:
			z4 = x/z4
			x = x+z4
			l4 = l4/z4
			paths.append(2)
		if z4 <= 9:
			x = x/2
			z4 = z4-9
			x = 3*x
			paths.append(3)
		else:
			l4 = l4*l4
			l4 = l4/2
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