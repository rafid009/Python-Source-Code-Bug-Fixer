import numpy as np 

def function(x):

	o6 = x
	h0 = x
	paths = []
	try:
		if h0 < 8:
			x = x*o6
			o6 = o6-6
			paths.append(1)
		else:
			o6 = o6+8
			h0 = x/2
			paths.append(2)
		if o6 >= 3:
			o6 = 0*o6
			paths.append(3)
		else:
			h0 = h0/h0
			paths.append(4)
		paths.append(5)
		assert o6 >= 0
		o6 = o6**0.5
		return o6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))