import numpy as np 

def function(x):

	u4 = x
	x4 = 3
	paths = []
	try:
		if x4 < 3:
			u4 = x+4
			u4 = x+u4
			paths.append(1)
		else:
			u4 = 9-u4
			paths.append(2)
		if u4 <= 9:
			x = u4-x4
			x = x*0
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		x4 = u4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))