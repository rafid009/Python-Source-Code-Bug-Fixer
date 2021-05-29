import numpy as np 

def function(x):

	u4 = 6
	i0 = 2
	paths = []
	try:
		if u4 > 5:
			i0 = i0/x
			paths.append(1)
		else:
			i0 = 1*i0
			paths.append(2)
		if x >= 3:
			u4 = x-i0
			i0 = i0-i0
			x = 3*3
			paths.append(3)
		else:
			x = x*i0
			paths.append(4)
		paths.append(5)
		assert i0 >= 0
		u4 = i0**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))