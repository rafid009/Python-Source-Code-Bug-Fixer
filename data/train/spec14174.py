import numpy as np 

def function(x):

	x4 = x
	y7 = x
	paths = []
	try:
		if x4 <= 6:
			x = x+x4
			paths.append(1)
		else:
			y7 = 1*x
			x = y7-5
			x = x/6
			paths.append(2)
		if x <= 7:
			y7 = x-y7
			x = 5+x
			paths.append(3)
		else:
			x4 = x4*1
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