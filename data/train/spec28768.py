import numpy as np 

def function(x):

	o0 = x
	h0 = x
	paths = []
	try:
		if x <= 4:
			x = 7-x
			paths.append(1)
		else:
			h0 = h0-3
			x = h0-2
			h0 = h0/9
			paths.append(2)
		if o0 > 5:
			h0 = 8+h0
			o0 = 6+o0
			paths.append(3)
		else:
			x = 7+x
			h0 = x*h0
			paths.append(4)
		paths.append(5)
		assert o0 >= 0
		x = o0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))