import numpy as np 

def function(x):

	z4 = x
	d3 = 6
	paths = []
	try:
		if x <= 2:
			d3 = 2-d3
			x = x*9
			z4 = z4-6
			paths.append(1)
		else:
			x = 0/x
			d3 = 9+d3
			paths.append(2)
		if x > 8:
			z4 = 2*z4
			z4 = d3*5
			paths.append(3)
		else:
			z4 = 6*0
			d3 = d3*d3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))