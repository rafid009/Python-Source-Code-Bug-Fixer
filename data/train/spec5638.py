import numpy as np 

def function(x):

	h0 = x
	y3 = 3
	paths = []
	try:
		if y3 >= 8:
			y3 = y3/9
			h0 = 7+9
			x = 0+7
			paths.append(1)
		else:
			x = 8-3
			x = 7-x
			y3 = x-y3
			paths.append(2)
		if y3 > 7:
			y3 = y3-7
			y3 = 1-h0
			paths.append(3)
		else:
			x = 7-x
			x = 0/1
			y3 = y3+x
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