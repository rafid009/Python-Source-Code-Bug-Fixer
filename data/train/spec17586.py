import numpy as np 

def function(x):

	z6 = x
	w1 = 2
	paths = []
	try:
		if x >= 5:
			w1 = w1/1
			paths.append(1)
		else:
			w1 = 0-w1
			x = x*0
			z6 = 9*z6
			paths.append(2)
		if x > 9:
			w1 = 0-w1
			paths.append(3)
		else:
			x = x-2
			z6 = z6-3
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