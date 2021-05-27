import numpy as np 

def function(x):

	o9 = x
	y5 = 6
	paths = []
	try:
		if x >= 3:
			y5 = y5-4
			x = x-4
			o9 = x/8
			paths.append(1)
		else:
			x = 0+x
			x = x-y5
			x = x-7
			paths.append(2)
		if o9 < 4:
			x = x+4
			paths.append(3)
		else:
			o9 = o9*o9
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