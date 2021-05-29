import numpy as np 

def function(x):

	w2 = x
	w5 = x
	paths = []
	try:
		if x <= 8:
			w2 = 6*w2
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if w5 <= 9:
			w5 = w5-w5
			paths.append(3)
		else:
			w2 = 8*w2
			x = x/w5
			x = 8+0
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