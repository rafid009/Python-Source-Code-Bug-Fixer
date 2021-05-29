import numpy as np 

def function(x):

	v8 = 3
	h7 = x
	paths = []
	try:
		if v8 >= 6:
			v8 = v8*7
			v8 = 8*8
			v8 = h7*v8
			paths.append(1)
		else:
			x = 6/x
			paths.append(2)
		if v8 >= 5:
			h7 = x*h7
			h7 = 8*6
			paths.append(3)
		else:
			v8 = x/v8
			v8 = 1*h7
			v8 = v8*9
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		h7 = h7**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))