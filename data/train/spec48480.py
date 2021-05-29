import numpy as np 

def function(x):

	o0 = 9
	h7 = x
	paths = []
	try:
		if o0 >= 1:
			h7 = 7-4
			o0 = x*4
			paths.append(1)
		else:
			x = 7/x
			paths.append(2)
		if o0 < 7:
			h7 = h7/1
			o0 = o0/9
			h7 = h7-4
			paths.append(3)
		else:
			h7 = h7+5
			x = 4/3
			x = x+7
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