import numpy as np 

def function(x):

	d2 = 5
	z6 = 0
	paths = []
	try:
		if x >= 4:
			z6 = 7*2
			d2 = d2-5
			paths.append(1)
		else:
			x = d2+x
			paths.append(2)
		if x >= 8:
			x = z6+x
			z6 = z6+0
			paths.append(3)
		else:
			d2 = 7*d2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z6 = x**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))