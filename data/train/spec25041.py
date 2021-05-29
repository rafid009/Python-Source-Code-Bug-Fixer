import numpy as np 

def function(x):

	w6 = x
	y2 = x
	paths = []
	try:
		if x < 8:
			w6 = 3+w6
			paths.append(1)
		else:
			x = x+w6
			paths.append(2)
		if w6 < 6:
			y2 = 5-0
			paths.append(3)
		else:
			w6 = 2*7
			y2 = x/6
			y2 = y2-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))