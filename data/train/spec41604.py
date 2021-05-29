import numpy as np 

def function(x):

	o5 = x
	h8 = x
	paths = []
	try:
		if o5 <= 6:
			o5 = x+8
			o5 = o5+o5
			h8 = h8*x
			paths.append(1)
		else:
			h8 = 0/h8
			h8 = 6*h8
			x = 8+x
			paths.append(2)
		if h8 > 2:
			x = 8/x
			paths.append(3)
		else:
			o5 = o5/9
			x = 3+9
			x = x+x
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		x = o5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))