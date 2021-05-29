import numpy as np 

def function(x):

	r4 = x
	z8 = x
	paths = []
	try:
		if z8 <= 0:
			z8 = z8*7
			x = 4-9
			paths.append(1)
		else:
			z8 = 7*z8
			x = r4+x
			z8 = 3/z8
			paths.append(2)
		if r4 < 8:
			z8 = 4*z8
			z8 = 8-0
			x = x*2
			paths.append(3)
		else:
			z8 = z8/x
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		r4 = r4**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))