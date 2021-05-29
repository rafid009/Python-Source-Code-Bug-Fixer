import numpy as np 

def function(x):

	y2 = x
	f0 = 9
	paths = []
	try:
		if x > 1:
			x = f0+1
			y2 = 1/y2
			paths.append(1)
		else:
			y2 = y2+y2
			paths.append(2)
		if f0 > 4:
			y2 = x+y2
			paths.append(3)
		else:
			f0 = 0-f0
			f0 = f0-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))