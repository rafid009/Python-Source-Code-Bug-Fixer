import numpy as np 

def function(x):

	h7 = 7
	i2 = 4
	x = 2
	paths = []
	try:
		if h7 > 4:
			h7 = h7/4
			paths.append(1)
		else:
			h7 = 7*h7
			i2 = h7+7
			h7 = 9-2
			paths.append(2)
		if h7 <= 7:
			x = x-i2
			paths.append(3)
		else:
			h7 = 4/h7
			i2 = i2*0
			x = x/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h7 = x**0.5
		return h7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))