import numpy as np 

def function(x):

	u7 = 0
	i0 = x
	paths = []
	try:
		if i0 < 8:
			i0 = i0+1
			paths.append(1)
		else:
			x = 1-i0
			paths.append(2)
		if u7 > 0:
			u7 = u7/1
			paths.append(3)
		else:
			u7 = i0-2
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