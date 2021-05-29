import numpy as np 

def function(x):

	y7 = x
	a8 = 9
	paths = []
	try:
		if x < 2:
			y7 = 1*y7
			paths.append(1)
		else:
			x = 1-5
			x = x*4
			y7 = x/8
			paths.append(2)
		if y7 >= 5:
			a8 = 2*a8
			y7 = y7/7
			paths.append(3)
		else:
			x = x-y7
			a8 = a8*a8
			a8 = 4+a8
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