import numpy as np 

def function(x):

	y2 = 0
	h0 = x
	paths = []
	try:
		if h0 >= 7:
			x = 1+y2
			paths.append(1)
		else:
			y2 = y2+7
			y2 = x/8
			paths.append(2)
		if y2 <= 3:
			h0 = h0*8
			paths.append(3)
		else:
			y2 = x-y2
			x = 8*5
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		x = h0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))