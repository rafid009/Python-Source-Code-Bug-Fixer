import numpy as np 

def function(x):

	i4 = x
	x1 = 7
	paths = []
	try:
		if i4 < 1:
			i4 = 6-i4
			x1 = x/7
			i4 = i4/2
			paths.append(1)
		else:
			i4 = 7/7
			x = 8/4
			paths.append(2)
		if x1 < 8:
			i4 = i4-4
			x = x*1
			paths.append(3)
		else:
			x1 = x1-8
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