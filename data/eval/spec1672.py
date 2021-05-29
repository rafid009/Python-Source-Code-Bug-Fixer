import numpy as np 

def function(x):

	x4 = 3
	v8 = 1
	paths = []
	try:
		if x < 5:
			x4 = 5-0
			x4 = x4-x
			x = x/x4
			paths.append(1)
		else:
			x4 = 1*1
			x = x-9
			paths.append(2)
		if x < 5:
			x = x-6
			v8 = x4*3
			paths.append(3)
		else:
			x = x4-x
			v8 = x-v8
			x4 = x4/v8
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x4 = x4**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))