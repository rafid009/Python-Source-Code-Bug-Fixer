import numpy as np 

def function(x):

	y0 = 9
	w3 = x
	paths = []
	try:
		if w3 > 2:
			y0 = 8-1
			x = x-0
			paths.append(1)
		else:
			y0 = 4+y0
			paths.append(2)
		if w3 >= 1:
			x = y0+x
			paths.append(3)
		else:
			w3 = w3*9
			y0 = y0-6
			w3 = w3+w3
			paths.append(4)
		paths.append(5)
		assert w3 >= 0
		x = w3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))