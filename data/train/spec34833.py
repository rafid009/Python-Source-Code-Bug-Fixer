import numpy as np 

def function(x):

	y5 = 2
	h0 = 1
	x = 1
	paths = []
	try:
		if y5 < 9:
			h0 = h0-6
			h0 = 9/h0
			paths.append(1)
		else:
			y5 = 1*y5
			y5 = y5*1
			paths.append(2)
		if y5 <= 5:
			y5 = 0+6
			y5 = 8-h0
			x = 3-x
			paths.append(3)
		else:
			y5 = 4-9
			x = 6+0
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