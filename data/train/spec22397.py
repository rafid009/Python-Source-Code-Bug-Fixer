import numpy as np 

def function(x):

	g9 = 3
	y7 = x
	paths = []
	try:
		if x < 7:
			x = 5-x
			x = 2/x
			paths.append(1)
		else:
			x = 8*x
			y7 = 8-8
			paths.append(2)
		if y7 >= 5:
			y7 = y7/2
			x = x*1
			y7 = g9-y7
			paths.append(3)
		else:
			y7 = x*2
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