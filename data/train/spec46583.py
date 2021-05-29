import numpy as np 

def function(x):

	t2 = x
	z0 = x
	paths = []
	try:
		if z0 >= 5:
			t2 = t2/z0
			paths.append(1)
		else:
			z0 = t2-5
			t2 = z0*2
			z0 = 8*x
			paths.append(2)
		if x >= 7:
			t2 = 2-t2
			z0 = 5*t2
			paths.append(3)
		else:
			t2 = 0+x
			x = 3+3
			paths.append(4)
		paths.append(5)
		assert z0 >= 0
		x = z0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))