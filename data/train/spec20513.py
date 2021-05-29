import numpy as np 

def function(x):

	j1 = 5
	u4 = x
	paths = []
	try:
		if j1 >= 0:
			x = x-6
			x = u4+5
			paths.append(1)
		else:
			u4 = u4-3
			x = x/x
			u4 = 2*u4
			paths.append(2)
		if u4 <= 2:
			j1 = j1-0
			paths.append(3)
		else:
			u4 = 9-3
			j1 = 4-j1
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x = u4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))