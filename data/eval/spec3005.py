import numpy as np 

def function(x):

	o0 = x
	h7 = x
	paths = []
	try:
		if o0 <= 6:
			h7 = h7+9
			paths.append(1)
		else:
			h7 = 8/h7
			x = 6-o0
			paths.append(2)
		if h7 >= 9:
			h7 = h7-3
			h7 = h7/8
			x = x/6
			paths.append(3)
		else:
			h7 = 3*h7
			o0 = 5+2
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		o0 = h7**0.5
		return o0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))