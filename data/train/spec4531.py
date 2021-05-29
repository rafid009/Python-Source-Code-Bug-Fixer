import numpy as np 

def function(x):

	v9 = 8
	u4 = 1
	paths = []
	try:
		if v9 > 1:
			x = x/1
			u4 = u4/8
			u4 = v9-u4
			paths.append(1)
		else:
			v9 = v9+7
			u4 = u4-v9
			paths.append(2)
		if v9 < 2:
			v9 = x/6
			x = x*1
			paths.append(3)
		else:
			u4 = v9-0
			v9 = u4-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v9 = x**0.5
		return v9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))