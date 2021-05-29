import numpy as np 

def function(x):

	z6 = 1
	w6 = 0
	paths = []
	try:
		if x > 6:
			z6 = z6/5
			paths.append(1)
		else:
			w6 = w6*w6
			x = x*8
			paths.append(2)
		if z6 >= 6:
			w6 = 3/5
			w6 = 3-w6
			paths.append(3)
		else:
			w6 = 2+z6
			z6 = 5+x
			w6 = 0/z6
			paths.append(4)
		paths.append(5)
		assert z6 >= 0
		x = z6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))