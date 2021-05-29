import numpy as np 

def function(x):

	b4 = x
	y8 = 5
	paths = []
	try:
		if b4 < 8:
			x = 7*b4
			paths.append(1)
		else:
			y8 = 0-y8
			y8 = y8+8
			x = x/y8
			paths.append(2)
		if x > 9:
			x = x+3
			x = 0+x
			paths.append(3)
		else:
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