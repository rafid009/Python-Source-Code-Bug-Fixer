import numpy as np 

def function(x):

	y1 = 1
	o8 = x
	x = 4
	paths = []
	try:
		if x <= 0:
			o8 = 6*o8
			y1 = y1*8
			paths.append(1)
		else:
			o8 = o8+7
			o8 = o8/1
			o8 = o8/1
			paths.append(2)
		if o8 < 7:
			x = x/6
			paths.append(3)
		else:
			y1 = 4-y1
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		o8 = o8**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))