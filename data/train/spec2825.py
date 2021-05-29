import numpy as np 

def function(x):

	w1 = x
	z4 = 5
	paths = []
	try:
		if x < 6:
			w1 = 5+w1
			x = x-6
			paths.append(1)
		else:
			x = z4*8
			paths.append(2)
		if w1 < 7:
			x = 8*x
			x = x-w1
			z4 = 1+z4
			paths.append(3)
		else:
			w1 = w1-z4
			w1 = w1*7
			w1 = 0/w1
			paths.append(4)
		paths.append(5)
		assert w1 >= 0
		z4 = w1**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))