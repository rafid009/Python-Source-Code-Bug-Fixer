import numpy as np 

def function(x):

	w6 = x
	h9 = 8
	paths = []
	try:
		if w6 > 8:
			w6 = w6-0
			w6 = w6*0
			h9 = 1*h9
			paths.append(1)
		else:
			h9 = 0/5
			paths.append(2)
		if h9 < 8:
			h9 = 5/6
			w6 = w6+h9
			paths.append(3)
		else:
			x = 8-6
			x = x+4
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