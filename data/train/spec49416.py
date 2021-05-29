import numpy as np 

def function(x):

	y8 = 0
	b4 = x
	paths = []
	try:
		if x <= 4:
			b4 = b4/4
			b4 = 8-y8
			b4 = 5+6
			paths.append(1)
		else:
			b4 = 8-b4
			paths.append(2)
		if x < 2:
			b4 = y8-b4
			x = x/8
			paths.append(3)
		else:
			y8 = y8-x
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))