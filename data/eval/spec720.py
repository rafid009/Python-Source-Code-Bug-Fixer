import numpy as np 

def function(x):

	k3 = x
	y1 = x
	paths = []
	try:
		if x > 7:
			k3 = 9/9
			y1 = 0/y1
			paths.append(1)
		else:
			y1 = 7+1
			paths.append(2)
		if x < 5:
			y1 = y1/y1
			paths.append(3)
		else:
			y1 = y1-k3
			x = x-k3
			y1 = 3/y1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))