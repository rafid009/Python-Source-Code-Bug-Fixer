import numpy as np 

def function(x):

	j9 = 8
	k1 = 2
	paths = []
	try:
		if j9 >= 6:
			k1 = j9/1
			j9 = 7-j9
			paths.append(1)
		else:
			x = 0-x
			j9 = 3/8
			paths.append(2)
		if x < 8:
			k1 = k1/3
			paths.append(3)
		else:
			x = 0/x
			j9 = j9+8
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