import numpy as np 

def function(x):

	y8 = x
	x4 = x
	paths = []
	try:
		if x <= 7:
			x = x+7
			paths.append(1)
		else:
			x4 = 4*8
			paths.append(2)
		if y8 <= 3:
			y8 = y8*y8
			y8 = x4+0
			y8 = y8*2
			paths.append(3)
		else:
			y8 = y8/6
			y8 = 8*1
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