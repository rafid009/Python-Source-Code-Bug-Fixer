import numpy as np 

def function(x):

	o3 = 6
	h8 = 8
	paths = []
	try:
		if h8 > 0:
			x = x/o3
			h8 = h8*1
			x = 3/x
			paths.append(1)
		else:
			h8 = x/h8
			x = x+0
			paths.append(2)
		if h8 >= 1:
			h8 = 5+h8
			o3 = 0*o3
			x = x+9
			paths.append(3)
		else:
			x = x/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o3 = x**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))