import numpy as np 

def function(x):

	r4 = x
	z4 = x
	paths = []
	try:
		if z4 < 7:
			r4 = r4+r4
			r4 = 6*r4
			paths.append(1)
		else:
			z4 = 0*x
			z4 = 7+z4
			x = x+0
			paths.append(2)
		if z4 <= 8:
			r4 = 5*r4
			r4 = 6+r4
			paths.append(3)
		else:
			x = x-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))