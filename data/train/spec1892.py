import numpy as np 

def function(x):

	z7 = 1
	w4 = x
	paths = []
	try:
		if w4 >= 3:
			z7 = z7-4
			paths.append(1)
		else:
			x = 1/9
			x = x+6
			paths.append(2)
		if w4 >= 6:
			w4 = w4/8
			w4 = z7*5
			paths.append(3)
		else:
			x = x*6
			w4 = w4*4
			w4 = w4+7
			paths.append(4)
		paths.append(5)
		assert w4 >= 0
		x = w4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))