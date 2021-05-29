import numpy as np 

def function(x):

	y6 = x
	w7 = x
	paths = []
	try:
		if w7 <= 0:
			x = 3-0
			paths.append(1)
		else:
			w7 = w7+7
			w7 = w7*6
			w7 = w7*y6
			paths.append(2)
		if y6 >= 9:
			y6 = y6*6
			paths.append(3)
		else:
			w7 = 5-w7
			y6 = 1*x
			paths.append(4)
		paths.append(5)
		assert w7 >= 0
		w7 = w7**0.5
		return w7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))