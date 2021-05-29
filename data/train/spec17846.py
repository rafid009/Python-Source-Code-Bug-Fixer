import numpy as np 

def function(x):

	r3 = 8
	h0 = x
	paths = []
	try:
		if r3 > 3:
			h0 = h0+r3
			r3 = r3+6
			paths.append(1)
		else:
			h0 = h0-0
			paths.append(2)
		if x <= 6:
			x = 7+7
			r3 = h0-3
			paths.append(3)
		else:
			h0 = h0*7
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))