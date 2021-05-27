import numpy as np 

def function(x):

	i4 = 5
	u2 = 1
	x = 5
	paths = []
	try:
		if x >= 8:
			x = 5+x
			u2 = x-3
			paths.append(1)
		else:
			i4 = 3-5
			paths.append(2)
		if u2 >= 8:
			x = i4*x
			i4 = 4-i4
			paths.append(3)
		else:
			i4 = i4*8
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))