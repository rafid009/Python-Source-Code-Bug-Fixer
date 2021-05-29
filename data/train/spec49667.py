import numpy as np 

def function(x):

	y2 = x
	b0 = 7
	paths = []
	try:
		if y2 > 3:
			x = x-x
			paths.append(1)
		else:
			x = b0-x
			x = x*y2
			paths.append(2)
		if y2 < 8:
			x = b0+y2
			paths.append(3)
		else:
			b0 = b0+b0
			b0 = 5-b0
			y2 = y2*x
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		b0 = y2**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))