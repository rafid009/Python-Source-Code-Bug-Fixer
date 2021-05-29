import numpy as np 

def function(x):

	y1 = x
	o9 = 8
	paths = []
	try:
		if o9 <= 4:
			y1 = y1/5
			x = o9*x
			y1 = y1/8
			paths.append(1)
		else:
			x = x+1
			y1 = x*y1
			paths.append(2)
		if x < 8:
			o9 = 2*5
			x = y1/1
			paths.append(3)
		else:
			o9 = x*4
			x = x*6
			o9 = o9+1
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