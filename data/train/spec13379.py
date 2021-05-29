import numpy as np 

def function(x):

	u4 = 1
	v0 = 1
	paths = []
	try:
		if u4 >= 0:
			v0 = u4-4
			u4 = u4/1
			u4 = 2/v0
			paths.append(1)
		else:
			u4 = x/u4
			paths.append(2)
		if v0 <= 3:
			u4 = 2/u4
			x = 6+2
			v0 = v0+9
			paths.append(3)
		else:
			u4 = 8/u4
			u4 = 7*2
			v0 = v0-5
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