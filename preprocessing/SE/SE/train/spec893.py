import numpy as np 

def function(x):

	y5 = x
	k1 = 8
	paths = []
	try:
		if y5 > 9:
			k1 = y5*k1
			paths.append(1)
		else:
			k1 = 0-0
			paths.append(2)
		if x <= 2:
			x = 7+x
			k1 = 2+k1
			paths.append(3)
		else:
			k1 = k1-5
			k1 = 6+k1
			y5 = y5-1
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