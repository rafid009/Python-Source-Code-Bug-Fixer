import numpy as np 

def function(x):

	z8 = x
	r2 = 1
	paths = []
	try:
		if z8 >= 8:
			r2 = r2*9
			paths.append(1)
		else:
			z8 = x+z8
			x = x+0
			paths.append(2)
		if z8 > 7:
			r2 = 0*0
			z8 = z8/z8
			paths.append(3)
		else:
			x = z8*x
			r2 = r2/z8
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		x = z8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))