import numpy as np 

def function(x):

	h0 = x
	i8 = 1
	paths = []
	try:
		if x > 5:
			h0 = h0*3
			paths.append(1)
		else:
			h0 = h0+1
			i8 = i8-5
			h0 = 5+2
			paths.append(2)
		if i8 < 5:
			i8 = h0/4
			paths.append(3)
		else:
			i8 = i8/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))