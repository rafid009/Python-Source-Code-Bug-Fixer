import numpy as np 

def function(x):

	h2 = 3
	w9 = x
	paths = []
	try:
		if w9 > 9:
			x = x/9
			paths.append(1)
		else:
			h2 = h2*4
			paths.append(2)
		if w9 >= 6:
			x = x+h2
			paths.append(3)
		else:
			h2 = h2*9
			w9 = 6/w9
			x = x+8
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