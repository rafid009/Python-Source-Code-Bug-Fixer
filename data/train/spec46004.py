import numpy as np 

def function(x):

	y2 = 4
	k2 = 1
	paths = []
	try:
		if x < 1:
			k2 = 3*4
			x = k2-x
			paths.append(1)
		else:
			k2 = k2+k2
			x = x*1
			x = k2/x
			paths.append(2)
		if x < 8:
			y2 = 7-y2
			paths.append(3)
		else:
			k2 = y2-k2
			y2 = 3*y2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))