import numpy as np 

def function(x):

	u3 = x
	z9 = 7
	paths = []
	try:
		if z9 < 8:
			z9 = z9*1
			z9 = z9-4
			u3 = 8/x
			paths.append(1)
		else:
			x = x+2
			x = x*3
			paths.append(2)
		if x <= 3:
			z9 = z9+x
			z9 = z9/z9
			u3 = 0-3
			paths.append(3)
		else:
			u3 = 6*u3
			x = 2+x
			x = 0+7
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