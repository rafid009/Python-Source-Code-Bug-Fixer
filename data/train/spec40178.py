import numpy as np 

def function(x):

	i4 = x
	u0 = 3
	paths = []
	try:
		if x >= 3:
			u0 = u0-9
			x = i4/x
			paths.append(1)
		else:
			i4 = i4/8
			paths.append(2)
		if u0 > 1:
			x = x/8
			paths.append(3)
		else:
			i4 = 3/i4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))