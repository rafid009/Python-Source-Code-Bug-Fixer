import numpy as np 

def function(x):

	y1 = x
	f0 = x
	paths = []
	try:
		if x <= 5:
			y1 = f0*y1
			f0 = x/y1
			y1 = y1*x
			paths.append(1)
		else:
			f0 = y1*y1
			x = 1*x
			paths.append(2)
		if y1 < 3:
			y1 = 8*y1
			paths.append(3)
		else:
			y1 = 6+x
			x = y1/x
			f0 = 6/9
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