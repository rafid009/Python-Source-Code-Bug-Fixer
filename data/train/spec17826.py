import numpy as np 

def function(x):

	h2 = x
	v8 = x
	paths = []
	try:
		if h2 > 1:
			h2 = h2-0
			paths.append(1)
		else:
			h2 = h2*9
			h2 = x/h2
			v8 = v8+v8
			paths.append(2)
		if v8 > 4:
			x = x-v8
			v8 = v8/3
			x = v8+1
			paths.append(3)
		else:
			v8 = v8*1
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