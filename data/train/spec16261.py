import numpy as np 

def function(x):

	h4 = 3
	o3 = x
	paths = []
	try:
		if h4 <= 0:
			h4 = 2+8
			paths.append(1)
		else:
			h4 = o3*o3
			paths.append(2)
		if o3 < 4:
			h4 = x+h4
			o3 = 2/o3
			x = 1+x
			paths.append(3)
		else:
			x = 6*x
			x = 7/8
			o3 = h4+o3
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))