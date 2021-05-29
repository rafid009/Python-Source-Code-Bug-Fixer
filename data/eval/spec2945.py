import numpy as np 

def function(x):

	b2 = x
	y5 = 4
	paths = []
	try:
		if b2 < 4:
			x = x+4
			x = 8-x
			x = x+6
			paths.append(1)
		else:
			b2 = b2*3
			x = 4-3
			paths.append(2)
		if y5 < 1:
			b2 = 3*b2
			y5 = y5*b2
			paths.append(3)
		else:
			y5 = 0/y5
			y5 = 4-3
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		y5 = b2**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))