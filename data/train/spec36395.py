import numpy as np 

def function(x):

	o1 = x
	y3 = 8
	paths = []
	try:
		if o1 < 7:
			y3 = 8+y3
			x = x*7
			paths.append(1)
		else:
			y3 = 6*o1
			paths.append(2)
		if o1 > 2:
			y3 = x/x
			paths.append(3)
		else:
			x = x-3
			o1 = 1-y3
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))