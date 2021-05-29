import numpy as np 

def function(x):

	z6 = 3
	w8 = x
	paths = []
	try:
		if w8 < 2:
			z6 = 2*0
			z6 = w8-z6
			z6 = z6+8
			paths.append(1)
		else:
			x = x/5
			w8 = w8/7
			paths.append(2)
		if z6 < 0:
			x = x/9
			paths.append(3)
		else:
			w8 = w8+3
			z6 = z6/5
			paths.append(4)
		paths.append(5)
		assert w8 >= 0
		x = w8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))