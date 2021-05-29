import numpy as np 

def function(x):

	h0 = x
	v4 = x
	paths = []
	try:
		if v4 <= 4:
			x = 1-6
			paths.append(1)
		else:
			h0 = 6+h0
			h0 = h0*1
			v4 = x/v4
			paths.append(2)
		if x > 1:
			x = v4+4
			paths.append(3)
		else:
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v4 = x**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))