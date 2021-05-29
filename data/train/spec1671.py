import numpy as np 

def function(x):

	y8 = 4
	w3 = x
	paths = []
	try:
		if y8 > 0:
			w3 = 7+5
			paths.append(1)
		else:
			x = 0*x
			w3 = w3-0
			x = x+2
			paths.append(2)
		if w3 <= 3:
			w3 = 8-w3
			x = w3/1
			y8 = 5-y8
			paths.append(3)
		else:
			w3 = 9*w3
			y8 = 0*6
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