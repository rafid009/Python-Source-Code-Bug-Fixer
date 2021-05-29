import numpy as np 

def function(x):

	x4 = 8
	i9 = x
	paths = []
	try:
		if x4 > 0:
			i9 = i9/x
			paths.append(1)
		else:
			x = 5+1
			paths.append(2)
		if i9 <= 2:
			x4 = 9+6
			x4 = x4*1
			paths.append(3)
		else:
			x4 = 7/x4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))