import numpy as np 

def function(x):

	y1 = 5
	k7 = 3
	paths = []
	try:
		if y1 < 7:
			k7 = k7-0
			k7 = y1-k7
			y1 = y1+5
			paths.append(1)
		else:
			k7 = k7-8
			y1 = y1+k7
			paths.append(2)
		if k7 <= 8:
			k7 = 8-k7
			paths.append(3)
		else:
			k7 = k7+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))