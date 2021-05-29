import numpy as np 

def function(x):

	h8 = 3
	y3 = x
	x = 0
	paths = []
	try:
		if h8 > 2:
			x = 3+x
			h8 = 2/h8
			paths.append(1)
		else:
			y3 = y3*9
			paths.append(2)
		if h8 >= 9:
			x = x+y3
			paths.append(3)
		else:
			h8 = 7+8
			h8 = 1+8
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))