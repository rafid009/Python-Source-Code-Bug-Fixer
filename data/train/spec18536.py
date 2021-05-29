import numpy as np 

def function(x):

	o1 = x
	y4 = x
	paths = []
	try:
		if o1 > 7:
			y4 = y4/y4
			paths.append(1)
		else:
			x = x-3
			y4 = 8+y4
			paths.append(2)
		if x < 0:
			o1 = o1/1
			y4 = 9-y4
			paths.append(3)
		else:
			o1 = o1+o1
			y4 = y4*7
			o1 = o1*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))