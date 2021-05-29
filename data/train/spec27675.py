import numpy as np 

def function(x):

	d3 = x
	z4 = x
	paths = []
	try:
		if x > 5:
			z4 = z4+x
			paths.append(1)
		else:
			z4 = x*5
			paths.append(2)
		if z4 < 3:
			d3 = d3-8
			d3 = d3*2
			paths.append(3)
		else:
			z4 = 1*z4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))