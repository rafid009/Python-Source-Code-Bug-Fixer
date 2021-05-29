import numpy as np 

def function(x):

	b0 = 6
	y6 = 6
	x = x
	paths = []
	try:
		if y6 <= 0:
			x = y6+4
			b0 = x/3
			x = 1*9
			paths.append(1)
		else:
			b0 = x-b0
			x = b0-x
			x = x+7
			paths.append(2)
		if y6 < 7:
			x = x+5
			x = 8*x
			x = 9+x
			paths.append(3)
		else:
			y6 = 0+y6
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