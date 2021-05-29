import numpy as np 

def function(x):

	y1 = x
	u7 = 8
	paths = []
	try:
		if x <= 8:
			u7 = u7-4
			y1 = y1-8
			y1 = y1/8
			paths.append(1)
		else:
			u7 = 7-y1
			paths.append(2)
		if x > 6:
			x = 4+x
			paths.append(3)
		else:
			y1 = y1-x
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))