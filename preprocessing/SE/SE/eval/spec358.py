import numpy as np 

def function(x):

	b4 = x
	y6 = 0
	paths = []
	try:
		if y6 < 1:
			y6 = b4/1
			y6 = x*9
			paths.append(1)
		else:
			b4 = 3*3
			b4 = 3/8
			paths.append(2)
		if y6 <= 0:
			y6 = y6-y6
			x = x+8
			b4 = b4/8
			paths.append(3)
		else:
			b4 = b4*5
			x = b4/5
			y6 = y6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))