import numpy as np 

def function(x):

	h4 = 8
	o6 = 1
	paths = []
	try:
		if h4 >= 7:
			o6 = 4/5
			h4 = o6/o6
			paths.append(1)
		else:
			o6 = o6*7
			x = 2-1
			o6 = 4+o6
			paths.append(2)
		if o6 > 1:
			x = 8+x
			h4 = 2+h4
			paths.append(3)
		else:
			h4 = 2*h4
			h4 = o6-h4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h4 = x**0.5
		return h4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))