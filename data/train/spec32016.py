import numpy as np 

def function(x):

	b4 = 2
	y1 = x
	paths = []
	try:
		if x > 2:
			b4 = b4-x
			x = 4*9
			y1 = x+b4
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if x < 5:
			x = x*b4
			y1 = 9+6
			b4 = b4*8
			paths.append(3)
		else:
			y1 = b4-8
			b4 = b4-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))