import numpy as np 

def function(x):

	y3 = x
	f9 = 6
	paths = []
	try:
		if x > 9:
			f9 = y3/5
			x = x/y3
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if y3 < 7:
			y3 = 8-y3
			paths.append(3)
		else:
			y3 = y3/3
			f9 = f9/8
			x = 5/8
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