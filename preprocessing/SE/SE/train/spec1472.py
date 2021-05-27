import numpy as np 

def function(x):

	r2 = x
	z8 = 5
	paths = []
	try:
		if x > 6:
			z8 = z8+0
			x = 6/x
			r2 = 5-r2
			paths.append(1)
		else:
			z8 = 5*z8
			z8 = 5+r2
			paths.append(2)
		if x >= 8:
			z8 = r2-5
			x = r2+9
			paths.append(3)
		else:
			x = 9*3
			x = r2/x
			paths.append(4)
		paths.append(5)
		assert z8 >= 0
		r2 = z8**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))