import numpy as np 

def function(x):

	h0 = x
	u3 = 0
	paths = []
	try:
		if h0 >= 3:
			h0 = 2/h0
			x = 4-6
			paths.append(1)
		else:
			x = 6+x
			x = 2+0
			paths.append(2)
		if x > 7:
			h0 = h0*u3
			paths.append(3)
		else:
			u3 = u3-h0
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