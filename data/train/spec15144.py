import numpy as np 

def function(x):

	h2 = 5
	v8 = x
	paths = []
	try:
		if x >= 2:
			v8 = 3-v8
			h2 = v8*7
			v8 = v8-h2
			paths.append(1)
		else:
			v8 = v8/5
			v8 = 9-v8
			v8 = 4-3
			paths.append(2)
		if x <= 8:
			x = 1-5
			h2 = h2+x
			v8 = v8-1
			paths.append(3)
		else:
			h2 = 6/h2
			x = x+7
			x = x-h2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))