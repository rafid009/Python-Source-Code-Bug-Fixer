import numpy as np 

def function(x):

	y1 = 1
	k4 = x
	paths = []
	try:
		if y1 > 3:
			k4 = 3/k4
			x = x+k4
			paths.append(1)
		else:
			k4 = 5-9
			paths.append(2)
		if x > 6:
			y1 = y1*3
			y1 = y1-0
			k4 = k4/7
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		y1 = k4**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))