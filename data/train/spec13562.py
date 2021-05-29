import numpy as np 

def function(x):

	z2 = x
	w1 = 1
	paths = []
	try:
		if z2 >= 1:
			x = x-7
			w1 = w1+2
			x = x-1
			paths.append(1)
		else:
			x = x-1
			z2 = z2/1
			paths.append(2)
		if z2 <= 7:
			w1 = z2/4
			z2 = w1*z2
			x = 7+w1
			paths.append(3)
		else:
			z2 = w1/w1
			z2 = w1-9
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