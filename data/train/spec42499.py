import numpy as np 

def function(x):

	d7 = 5
	y8 = 6
	paths = []
	try:
		if d7 <= 4:
			y8 = y8*x
			y8 = 7+y8
			y8 = y8-4
			paths.append(1)
		else:
			x = 4/x
			paths.append(2)
		if d7 < 9:
			d7 = d7-4
			paths.append(3)
		else:
			y8 = 2+y8
			x = x/6
			x = 5+3
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