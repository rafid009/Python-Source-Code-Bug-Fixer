import numpy as np 

def function(x):

	q4 = x
	o8 = x
	x = x
	paths = []
	try:
		if q4 < 1:
			x = o8+x
			x = 7*x
			x = o8+7
			paths.append(1)
		else:
			o8 = o8/6
			paths.append(2)
		if q4 < 2:
			q4 = q4-6
			paths.append(3)
		else:
			o8 = o8*o8
			o8 = x+6
			q4 = 3*q4
			paths.append(4)
		paths.append(5)
		assert q4 >= 0
		x = q4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))