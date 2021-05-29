import numpy as np 

def function(x):

	v9 = x
	u7 = x
	paths = []
	try:
		if x >= 0:
			u7 = v9+v9
			x = 8/2
			paths.append(1)
		else:
			x = x/3
			u7 = u7+8
			x = u7/x
			paths.append(2)
		if v9 > 0:
			x = x-1
			u7 = v9*1
			u7 = x+u7
			paths.append(3)
		else:
			u7 = u7+0
			v9 = v9*9
			v9 = v9-3
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))