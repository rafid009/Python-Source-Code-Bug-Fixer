import numpy as np 

def function(x):

	v7 = 6
	y7 = 4
	x = 4
	paths = []
	try:
		if x >= 9:
			x = y7*x
			v7 = v7*v7
			paths.append(1)
		else:
			y7 = 1-v7
			v7 = 6/6
			paths.append(2)
		if v7 <= 0:
			y7 = 3-y7
			v7 = 5-1
			paths.append(3)
		else:
			v7 = 8/v7
			x = x+3
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		y7 = y7**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))