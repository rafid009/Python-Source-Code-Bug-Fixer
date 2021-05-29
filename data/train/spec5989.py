import numpy as np 

def function(x):

	y4 = x
	b0 = x
	paths = []
	try:
		if y4 < 2:
			y4 = 6-y4
			paths.append(1)
		else:
			x = 1-x
			y4 = y4*1
			paths.append(2)
		if y4 >= 8:
			x = x+2
			b0 = 3*8
			paths.append(3)
		else:
			b0 = b0-1
			y4 = y4*b0
			x = y4/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))