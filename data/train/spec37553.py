import numpy as np 

def function(x):

	o8 = x
	x7 = 1
	paths = []
	try:
		if x < 6:
			x = 0+x
			o8 = 5*o8
			x7 = x/x7
			paths.append(1)
		else:
			x7 = x7-o8
			x = 4-1
			paths.append(2)
		if o8 >= 8:
			o8 = 6*5
			x = 7+x
			o8 = o8*2
			paths.append(3)
		else:
			x = 4-x7
			o8 = x7+o8
			paths.append(4)
		paths.append(5)
		assert x7 >= 0
		x7 = x7**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))