import numpy as np 

def function(x):

	w3 = x
	h2 = 5
	paths = []
	try:
		if x > 8:
			w3 = w3+9
			paths.append(1)
		else:
			h2 = h2*3
			paths.append(2)
		if h2 >= 0:
			w3 = w3/w3
			paths.append(3)
		else:
			h2 = h2+1
			x = x+6
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