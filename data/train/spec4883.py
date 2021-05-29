import numpy as np 

def function(x):

	y7 = x
	b4 = 4
	paths = []
	try:
		if y7 < 7:
			b4 = b4-y7
			y7 = y7/b4
			paths.append(1)
		else:
			b4 = 8+5
			y7 = x-1
			paths.append(2)
		if x > 2:
			x = x+2
			paths.append(3)
		else:
			b4 = b4-x
			y7 = y7/2
			b4 = b4*6
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