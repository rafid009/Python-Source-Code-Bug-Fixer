import numpy as np 

def function(x):

	z4 = 6
	w3 = 6
	paths = []
	try:
		if w3 <= 8:
			z4 = z4/z4
			x = x+0
			w3 = 5*w3
			paths.append(1)
		else:
			w3 = w3*0
			paths.append(2)
		if w3 >= 1:
			z4 = 6-8
			x = x/x
			paths.append(3)
		else:
			x = x*x
			z4 = w3/z4
			paths.append(4)
		paths.append(5)
		assert z4 >= 0
		z4 = z4**0.5
		return z4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))