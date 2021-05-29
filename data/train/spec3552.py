import numpy as np 

def function(x):

	n7 = x
	y7 = 0
	x = x
	paths = []
	try:
		if x >= 6:
			n7 = n7/5
			paths.append(1)
		else:
			n7 = 8+n7
			y7 = y7*2
			paths.append(2)
		if x < 0:
			x = 7+x
			paths.append(3)
		else:
			n7 = n7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y7 = x**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))