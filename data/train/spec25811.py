import numpy as np 

def function(x):

	z6 = 3
	f1 = 1
	paths = []
	try:
		if x <= 9:
			z6 = 1+9
			z6 = 0-x
			paths.append(1)
		else:
			f1 = 1+6
			x = f1-x
			z6 = 3/8
			paths.append(2)
		if z6 >= 7:
			x = 2*x
			paths.append(3)
		else:
			f1 = f1+0
			z6 = 6+z6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))