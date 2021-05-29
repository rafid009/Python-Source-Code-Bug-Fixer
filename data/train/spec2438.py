import numpy as np 

def function(x):

	z6 = x
	l0 = 8
	paths = []
	try:
		if z6 < 0:
			l0 = 7-3
			x = l0+2
			l0 = l0/x
			paths.append(1)
		else:
			x = 8+6
			z6 = 8/z6
			z6 = z6*0
			paths.append(2)
		if x < 6:
			x = x*5
			l0 = 7+l0
			z6 = z6*9
			paths.append(3)
		else:
			z6 = l0+z6
			l0 = 8+l0
			x = x+5
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		l0 = z6**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))