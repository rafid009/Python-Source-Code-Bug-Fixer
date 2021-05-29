import numpy as np 

def function(x):

	y2 = x
	k7 = 1
	paths = []
	try:
		if y2 >= 3:
			k7 = 4+k7
			paths.append(1)
		else:
			x = x*9
			paths.append(2)
		if y2 > 7:
			y2 = y2-k7
			paths.append(3)
		else:
			y2 = y2/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))