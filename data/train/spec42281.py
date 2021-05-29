import numpy as np 

def function(x):

	w7 = 4
	y1 = 3
	paths = []
	try:
		if w7 <= 1:
			x = x-y1
			paths.append(1)
		else:
			y1 = w7/3
			x = y1-3
			y1 = y1-5
			paths.append(2)
		if y1 >= 3:
			x = 7*2
			w7 = 0/w7
			x = x/w7
			paths.append(3)
		else:
			y1 = w7+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))