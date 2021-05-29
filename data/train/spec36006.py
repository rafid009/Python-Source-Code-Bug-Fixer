import numpy as np 

def function(x):

	o5 = x
	h8 = 1
	paths = []
	try:
		if x > 0:
			h8 = x+o5
			x = 4-x
			paths.append(1)
		else:
			x = 8+o5
			h8 = 6-h8
			o5 = x*4
			paths.append(2)
		if h8 >= 7:
			o5 = o5/9
			paths.append(3)
		else:
			h8 = o5*0
			h8 = h8-h8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h8 = x**0.5
		return h8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))