import numpy as np 

def function(x):

	y1 = 2
	o5 = 3
	paths = []
	try:
		if o5 >= 0:
			x = 7*x
			paths.append(1)
		else:
			x = 2-x
			paths.append(2)
		if x >= 9:
			o5 = 1+y1
			paths.append(3)
		else:
			y1 = x*y1
			y1 = y1/3
			x = y1/6
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))