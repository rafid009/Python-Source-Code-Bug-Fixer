import numpy as np 

def function(x):

	z9 = 6
	d3 = 9
	paths = []
	try:
		if z9 <= 9:
			d3 = d3*x
			z9 = x-0
			z9 = z9+6
			paths.append(1)
		else:
			z9 = 0+z9
			paths.append(2)
		if z9 < 9:
			z9 = x*9
			paths.append(3)
		else:
			x = x*d3
			z9 = z9+1
			paths.append(4)
		paths.append(5)
		assert z9 >= 0
		x = z9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))