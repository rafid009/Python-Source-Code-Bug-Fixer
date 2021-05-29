import numpy as np 

def function(x):

	z8 = x
	w9 = x
	paths = []
	try:
		if w9 > 5:
			x = x+w9
			w9 = x-7
			w9 = w9+x
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if z8 <= 0:
			z8 = 9+x
			z8 = z8-8
			paths.append(3)
		else:
			x = x/1
			z8 = w9+4
			w9 = z8/8
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