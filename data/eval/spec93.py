import numpy as np 

def function(x):

	b6 = 4
	y2 = x
	paths = []
	try:
		if x > 1:
			b6 = b6-6
			paths.append(1)
		else:
			b6 = 5-b6
			b6 = b6+2
			paths.append(2)
		if x <= 0:
			y2 = 6*y2
			b6 = 1*y2
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))