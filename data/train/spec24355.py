import numpy as np 

def function(x):

	h6 = x
	o3 = x
	x = 6
	paths = []
	try:
		if h6 <= 0:
			h6 = 0+h6
			x = 4+x
			o3 = o3-1
			paths.append(1)
		else:
			x = 2-x
			h6 = h6*x
			paths.append(2)
		if o3 <= 3:
			x = 4*4
			x = 9-o3
			h6 = o3-x
			paths.append(3)
		else:
			o3 = h6-o3
			x = x+9
			h6 = h6/5
			paths.append(4)
		paths.append(5)
		assert h6 >= 0
		o3 = h6**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))