import numpy as np 

def function(x):

	t0 = 1
	z5 = x
	paths = []
	try:
		if z5 <= 9:
			x = 1+8
			x = 9-x
			z5 = z5*t0
			paths.append(1)
		else:
			z5 = 4*z5
			paths.append(2)
		if z5 > 9:
			z5 = 0+3
			paths.append(3)
		else:
			x = t0+x
			x = x+0
			t0 = 1-0
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))