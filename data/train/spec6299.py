import numpy as np 

def function(x):

	u8 = 2
	h4 = x
	paths = []
	try:
		if x > 4:
			h4 = h4*5
			x = 0/2
			h4 = 2/9
			paths.append(1)
		else:
			h4 = h4+8
			x = 1+x
			u8 = 9-u8
			paths.append(2)
		if x <= 9:
			x = 9*h4
			paths.append(3)
		else:
			x = x/x
			h4 = x-9
			paths.append(4)
		paths.append(5)
		assert h4 >= 0
		x = h4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))