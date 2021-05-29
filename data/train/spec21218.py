import numpy as np 

def function(x):

	h3 = x
	w1 = 2
	paths = []
	try:
		if w1 > 3:
			w1 = 3/w1
			paths.append(1)
		else:
			h3 = h3-1
			paths.append(2)
		if w1 > 2:
			h3 = h3/2
			x = h3*7
			x = x/8
			paths.append(3)
		else:
			w1 = h3/h3
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