import numpy as np 

def function(x):

	x4 = x
	i7 = 8
	paths = []
	try:
		if x < 5:
			i7 = 4*1
			paths.append(1)
		else:
			x = x4/i7
			x = x+8
			paths.append(2)
		if x4 <= 4:
			x4 = 5/x4
			paths.append(3)
		else:
			i7 = 8/i7
			i7 = 4/8
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x4 >= 0
		x = x4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))