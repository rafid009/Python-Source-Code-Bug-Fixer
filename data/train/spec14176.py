import numpy as np 

def function(x):

	z4 = 1
	l5 = x
	paths = []
	try:
		if z4 >= 8:
			x = l5-7
			paths.append(1)
		else:
			l5 = 6*6
			z4 = x*l5
			l5 = x*l5
			paths.append(2)
		if l5 >= 6:
			l5 = z4-2
			l5 = 7-3
			l5 = l5+6
			paths.append(3)
		else:
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		x = z4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))