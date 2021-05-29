import numpy as np 

def function(x):

	b0 = 5
	u4 = x
	x = 5
	paths = []
	try:
		if b0 > 2:
			b0 = 4*x
			b0 = x/7
			x = u4+8
			paths.append(1)
		else:
			b0 = b0*8
			paths.append(2)
		if x >= 9:
			u4 = u4-u4
			b0 = b0-6
			paths.append(3)
		else:
			x = x-b0
			b0 = u4+b0
			x = x/3
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		x = b0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))