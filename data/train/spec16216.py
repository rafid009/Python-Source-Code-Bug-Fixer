import numpy as np 

def function(x):

	z4 = 8
	w6 = x
	paths = []
	try:
		if w6 < 6:
			z4 = z4*3
			x = 7/x
			paths.append(1)
		else:
			z4 = 5-z4
			x = x+0
			paths.append(2)
		if z4 <= 0:
			w6 = x*w6
			w6 = z4-9
			z4 = 9*3
			paths.append(3)
		else:
			w6 = w6*9
			paths.append(4)
		paths.append(5)
		assert w6 >= 0
		x = w6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))