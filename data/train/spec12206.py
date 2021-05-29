import numpy as np 

def function(x):

	v8 = x
	h7 = 4
	paths = []
	try:
		if h7 > 4:
			v8 = v8-6
			v8 = v8/7
			paths.append(1)
		else:
			x = h7/v8
			h7 = h7-4
			paths.append(2)
		if v8 > 6:
			h7 = 6*h7
			h7 = h7-1
			paths.append(3)
		else:
			v8 = 9+v8
			h7 = 7-h7
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))