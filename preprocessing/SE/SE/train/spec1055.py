import numpy as np 

def function(x):

	i8 = 4
	h7 = 5
	paths = []
	try:
		if i8 <= 1:
			x = x/4
			x = x-9
			i8 = i8+i8
			paths.append(1)
		else:
			h7 = h7-h7
			i8 = 1*i8
			paths.append(2)
		if x > 6:
			i8 = 6-i8
			x = x-h7
			paths.append(3)
		else:
			i8 = h7/4
			h7 = i8*h7
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