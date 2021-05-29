import numpy as np 

def function(x):

	z5 = 0
	b0 = x
	paths = []
	try:
		if z5 <= 0:
			b0 = 0-b0
			x = x-0
			b0 = b0*4
			paths.append(1)
		else:
			b0 = z5/b0
			paths.append(2)
		if x < 3:
			b0 = 9*b0
			x = 2+x
			paths.append(3)
		else:
			x = x-0
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