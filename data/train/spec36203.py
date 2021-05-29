import numpy as np 

def function(x):

	y2 = 3
	b4 = 4
	paths = []
	try:
		if y2 > 2:
			x = 2*x
			b4 = b4/b4
			y2 = 2-6
			paths.append(1)
		else:
			b4 = 9*b4
			b4 = x+b4
			paths.append(2)
		if x <= 2:
			b4 = b4-8
			x = 0-3
			b4 = 8/b4
			paths.append(3)
		else:
			b4 = 1/b4
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		b4 = y2**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))