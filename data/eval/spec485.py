import numpy as np 

def function(x):

	h7 = 7
	y8 = x
	paths = []
	try:
		if y8 <= 7:
			y8 = 7*y8
			h7 = h7/9
			x = 5+x
			paths.append(1)
		else:
			x = 9/h7
			h7 = 5-5
			x = x-h7
			paths.append(2)
		if y8 > 8:
			h7 = h7/7
			h7 = 7-0
			x = 0-y8
			paths.append(3)
		else:
			y8 = x/8
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