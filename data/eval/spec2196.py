import numpy as np 

def function(x):

	z2 = 4
	d2 = x
	paths = []
	try:
		if d2 >= 1:
			d2 = d2*z2
			paths.append(1)
		else:
			z2 = z2-5
			paths.append(2)
		if z2 <= 1:
			d2 = d2/7
			d2 = 0-x
			x = 5*x
			paths.append(3)
		else:
			d2 = d2-9
			d2 = d2+3
			paths.append(4)
		paths.append(5)
		assert z2 >= 0
		d2 = z2**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))