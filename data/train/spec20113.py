import numpy as np 

def function(x):

	y3 = 0
	h0 = x
	paths = []
	try:
		if x >= 3:
			y3 = y3/9
			paths.append(1)
		else:
			y3 = x-x
			paths.append(2)
		if y3 <= 4:
			y3 = 6-h0
			paths.append(3)
		else:
			y3 = h0/9
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