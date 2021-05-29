import numpy as np 

def function(x):

	x4 = x
	i7 = x
	paths = []
	try:
		if x > 4:
			x4 = 8/x4
			x4 = 9+x4
			i7 = 6*i7
			paths.append(1)
		else:
			x = 8+x
			i7 = i7*5
			paths.append(2)
		if x4 > 1:
			x4 = 2*3
			paths.append(3)
		else:
			i7 = i7-i7
			x = x4+x
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))