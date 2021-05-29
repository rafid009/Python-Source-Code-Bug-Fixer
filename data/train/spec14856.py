import numpy as np 

def function(x):

	z6 = x
	d3 = 7
	paths = []
	try:
		if z6 < 5:
			x = 1*3
			paths.append(1)
		else:
			d3 = d3*8
			d3 = d3/x
			paths.append(2)
		if z6 > 8:
			d3 = 8+9
			z6 = 7*z6
			paths.append(3)
		else:
			d3 = d3+d3
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