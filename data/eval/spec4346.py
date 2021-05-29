import numpy as np 

def function(x):

	h6 = x
	w1 = 9
	paths = []
	try:
		if w1 > 9:
			w1 = 5/1
			x = w1/x
			paths.append(1)
		else:
			w1 = w1*5
			h6 = 2+h6
			x = x+x
			paths.append(2)
		if h6 > 6:
			w1 = 3+h6
			x = x+4
			h6 = 9*9
			paths.append(3)
		else:
			h6 = x-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		w1 = x**0.5
		return w1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))