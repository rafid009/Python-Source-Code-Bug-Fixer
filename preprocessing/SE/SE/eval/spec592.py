import numpy as np 

def function(x):

	w5 = 4
	h3 = x
	x = x
	paths = []
	try:
		if h3 < 0:
			w5 = w5-h3
			x = 8+5
			paths.append(1)
		else:
			w5 = x*4
			paths.append(2)
		if x >= 4:
			w5 = 9-5
			x = x/x
			paths.append(3)
		else:
			x = 2*x
			w5 = w5/w5
			paths.append(4)
		paths.append(5)
		assert h3 >= 0
		h3 = h3**0.5
		return h3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))