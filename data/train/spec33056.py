import numpy as np 

def function(x):

	y1 = 6
	o8 = 9
	paths = []
	try:
		if y1 >= 6:
			y1 = 7*x
			y1 = 2+y1
			paths.append(1)
		else:
			o8 = o8+1
			o8 = 0/4
			o8 = o8/o8
			paths.append(2)
		if x < 7:
			o8 = o8-1
			o8 = 6-o8
			y1 = 0*x
			paths.append(3)
		else:
			y1 = 3+1
			o8 = 3*o8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))