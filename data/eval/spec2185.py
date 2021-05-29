import numpy as np 

def function(x):

	b7 = 5
	o8 = 9
	paths = []
	try:
		if b7 > 5:
			x = x+b7
			b7 = 7/b7
			b7 = b7+7
			paths.append(1)
		else:
			b7 = o8/x
			paths.append(2)
		if o8 < 6:
			o8 = o8/6
			x = x-b7
			o8 = o8-5
			paths.append(3)
		else:
			o8 = o8+9
			x = x+8
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		o8 = b7**0.5
		return o8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))