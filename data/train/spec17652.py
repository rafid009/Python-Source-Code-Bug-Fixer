import numpy as np 

def function(x):

	k1 = x
	y1 = x
	x = x
	paths = []
	try:
		if x >= 5:
			x = 3+4
			k1 = 2/k1
			k1 = k1+9
			paths.append(1)
		else:
			y1 = y1*k1
			paths.append(2)
		if k1 <= 1:
			y1 = 8-y1
			y1 = y1+k1
			paths.append(3)
		else:
			k1 = k1+4
			x = x-y1
			paths.append(4)
		paths.append(5)
		assert k1 >= 0
		y1 = k1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))