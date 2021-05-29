import numpy as np 

def function(x):

	k2 = 6
	y3 = x
	paths = []
	try:
		if x <= 3:
			y3 = y3+x
			paths.append(1)
		else:
			x = 9-x
			y3 = 2+x
			y3 = 6-y3
			paths.append(2)
		if x <= 0:
			y3 = y3-y3
			paths.append(3)
		else:
			y3 = 5*8
			k2 = k2/k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))