import numpy as np 

def function(x):

	y1 = 5
	w3 = x
	paths = []
	try:
		if w3 <= 5:
			w3 = w3/2
			y1 = 1/5
			w3 = w3*9
			paths.append(1)
		else:
			x = x*w3
			w3 = w3-1
			paths.append(2)
		if w3 >= 1:
			y1 = 7/y1
			x = x+x
			w3 = 7/w3
			paths.append(3)
		else:
			w3 = y1*w3
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