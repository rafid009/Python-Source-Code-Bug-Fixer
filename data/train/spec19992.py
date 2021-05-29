import numpy as np 

def function(x):

	f7 = x
	y5 = 1
	paths = []
	try:
		if x < 9:
			f7 = 4*8
			y5 = y5/x
			y5 = 8/1
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x <= 9:
			f7 = 7/f7
			paths.append(3)
		else:
			f7 = f7/x
			x = x-3
			x = 5-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y5 = x**0.5
		return y5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))