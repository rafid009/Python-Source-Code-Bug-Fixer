import numpy as np 

def function(x):

	d1 = x
	z6 = 4
	paths = []
	try:
		if d1 >= 3:
			z6 = 7-x
			d1 = 7-d1
			paths.append(1)
		else:
			d1 = 7+d1
			paths.append(2)
		if x <= 8:
			z6 = 0*x
			z6 = z6/x
			x = 9+9
			paths.append(3)
		else:
			x = x+1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))