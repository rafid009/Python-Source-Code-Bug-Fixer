import numpy as np 

def function(x):

	y4 = x
	w3 = x
	paths = []
	try:
		if y4 <= 1:
			w3 = y4*x
			y4 = 8*y4
			paths.append(1)
		else:
			x = 3*x
			paths.append(2)
		if w3 >= 1:
			x = 4-2
			w3 = w3-8
			w3 = 7+w3
			paths.append(3)
		else:
			w3 = w3*y4
			w3 = w3/y4
			y4 = w3+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))