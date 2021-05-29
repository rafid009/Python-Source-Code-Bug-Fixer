import numpy as np 

def function(x):

	h0 = x
	u6 = 0
	paths = []
	try:
		if x > 8:
			h0 = 4*9
			paths.append(1)
		else:
			h0 = x+h0
			u6 = h0-5
			x = h0*4
			paths.append(2)
		if x <= 8:
			u6 = 3+u6
			h0 = x/1
			paths.append(3)
		else:
			h0 = 7/h0
			x = x-u6
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		x = u6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))