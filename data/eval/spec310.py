import numpy as np 

def function(x):

	z9 = 9
	u3 = 1
	paths = []
	try:
		if u3 > 7:
			x = x/u3
			paths.append(1)
		else:
			u3 = u3-5
			paths.append(2)
		if z9 > 8:
			z9 = z9/1
			z9 = z9/z9
			paths.append(3)
		else:
			z9 = 2/z9
			z9 = 5-z9
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