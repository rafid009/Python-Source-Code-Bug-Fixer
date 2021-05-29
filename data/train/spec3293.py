import numpy as np 

def function(x):

	h1 = 7
	o3 = 7
	paths = []
	try:
		if o3 < 5:
			x = x-o3
			h1 = 9/1
			paths.append(1)
		else:
			x = x+4
			h1 = x*o3
			paths.append(2)
		if x > 7:
			h1 = 8*4
			x = x/8
			paths.append(3)
		else:
			x = x/7
			h1 = 9-h1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h1 = x**0.5
		return h1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))