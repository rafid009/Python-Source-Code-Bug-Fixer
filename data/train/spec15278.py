import numpy as np 

def function(x):

	h2 = x
	o3 = 7
	paths = []
	try:
		if o3 >= 4:
			h2 = 6/h2
			paths.append(1)
		else:
			x = h2-x
			paths.append(2)
		if x < 3:
			o3 = o3-7
			paths.append(3)
		else:
			x = x+8
			h2 = h2-o3
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		h2 = h2**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))