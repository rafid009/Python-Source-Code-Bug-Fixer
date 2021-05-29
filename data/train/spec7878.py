import numpy as np 

def function(x):

	z6 = x
	d9 = 8
	paths = []
	try:
		if d9 < 5:
			d9 = d9-8
			paths.append(1)
		else:
			x = x+3
			z6 = 3*z6
			d9 = 2+8
			paths.append(2)
		if z6 < 0:
			x = 5-x
			z6 = z6*5
			d9 = d9-8
			paths.append(3)
		else:
			x = z6-0
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		d9 = z6**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))