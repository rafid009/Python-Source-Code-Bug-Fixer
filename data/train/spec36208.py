import numpy as np 

def function(x):

	o9 = x
	h0 = x
	paths = []
	try:
		if o9 > 4:
			o9 = o9*o9
			paths.append(1)
		else:
			o9 = 7/o9
			h0 = h0+9
			paths.append(2)
		if o9 > 7:
			x = x+h0
			h0 = o9*2
			o9 = o9-4
			paths.append(3)
		else:
			h0 = 8*h0
			o9 = 0/o9
			x = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h0 = x**0.5
		return h0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))