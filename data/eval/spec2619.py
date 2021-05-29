import numpy as np 

def function(x):

	b0 = x
	y7 = x
	paths = []
	try:
		if x <= 5:
			y7 = b0*y7
			paths.append(1)
		else:
			b0 = 4/x
			paths.append(2)
		if b0 >= 9:
			b0 = b0+b0
			x = x/x
			paths.append(3)
		else:
			y7 = 0*8
			x = y7-x
			y7 = 7+y7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))