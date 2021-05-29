import numpy as np 

def function(x):

	h8 = 3
	y3 = 3
	paths = []
	try:
		if x < 1:
			y3 = y3*1
			paths.append(1)
		else:
			x = 8*9
			paths.append(2)
		if x >= 1:
			y3 = y3-7
			paths.append(3)
		else:
			x = 8+x
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