import numpy as np 

def function(x):

	t3 = x
	z2 = 2
	x = 4
	paths = []
	try:
		if x > 5:
			z2 = z2*3
			z2 = 0*z2
			t3 = 5+t3
			paths.append(1)
		else:
			x = 2/x
			paths.append(2)
		if z2 <= 8:
			x = t3+3
			t3 = 4*t3
			paths.append(3)
		else:
			z2 = 0-z2
			x = 7/t3
			x = x+x
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