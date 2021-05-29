import numpy as np 

def function(x):

	h8 = x
	o0 = 4
	paths = []
	try:
		if o0 >= 1:
			h8 = 7/5
			o0 = 0*o0
			h8 = 5-x
			paths.append(1)
		else:
			o0 = 9*3
			h8 = 9+8
			paths.append(2)
		if o0 < 2:
			o0 = o0-0
			h8 = h8-0
			paths.append(3)
		else:
			o0 = o0+x
			o0 = o0/h8
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		x = h8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))