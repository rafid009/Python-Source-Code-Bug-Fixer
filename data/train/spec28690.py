import numpy as np 

def function(x):

	a5 = 0
	z2 = x
	paths = []
	try:
		if z2 <= 1:
			a5 = 5+z2
			paths.append(1)
		else:
			x = x+x
			x = z2-7
			a5 = z2-x
			paths.append(2)
		if z2 >= 7:
			a5 = a5/a5
			x = x*a5
			a5 = 2*a5
			paths.append(3)
		else:
			z2 = a5/z2
			x = x*x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		z2 = a5**0.5
		return z2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))