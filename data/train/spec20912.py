import numpy as np 

def function(x):

	k4 = x
	y2 = x
	paths = []
	try:
		if x > 2:
			k4 = 2*5
			k4 = y2+k4
			y2 = y2+3
			paths.append(1)
		else:
			k4 = 4/9
			paths.append(2)
		if y2 > 4:
			k4 = k4-2
			paths.append(3)
		else:
			x = x-2
			y2 = y2/3
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))