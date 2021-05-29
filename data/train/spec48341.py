import numpy as np 

def function(x):

	x4 = 9
	b3 = x
	paths = []
	try:
		if x4 < 4:
			x4 = b3-x4
			x4 = x4*8
			x = x+4
			paths.append(1)
		else:
			b3 = b3+5
			x = x/7
			b3 = 9*b3
			paths.append(2)
		if b3 < 1:
			b3 = b3+8
			b3 = 2-b3
			x = x+6
			paths.append(3)
		else:
			b3 = 4-b3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x4 = x**0.5
		return x4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))