import numpy as np 

def function(x):

	z6 = x
	d2 = 1
	paths = []
	try:
		if z6 >= 1:
			d2 = 5-z6
			paths.append(1)
		else:
			x = x+5
			d2 = d2*0
			z6 = z6-5
			paths.append(2)
		if x > 4:
			z6 = x*d2
			z6 = 6*d2
			paths.append(3)
		else:
			z6 = 6/z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		z6 = z6**0.5
		return z6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))