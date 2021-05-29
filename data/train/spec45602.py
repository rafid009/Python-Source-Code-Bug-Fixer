import numpy as np 

def function(x):

	o1 = 4
	y6 = x
	paths = []
	try:
		if x <= 0:
			y6 = 3/y6
			y6 = y6-8
			x = y6/1
			paths.append(1)
		else:
			y6 = y6-y6
			paths.append(2)
		if o1 < 6:
			x = x/5
			x = 0-o1
			x = 8*x
			paths.append(3)
		else:
			y6 = o1+y6
			o1 = o1+o1
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		o1 = y6**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))