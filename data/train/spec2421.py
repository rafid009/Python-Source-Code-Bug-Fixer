import numpy as np 

def function(x):

	x0 = 9
	o8 = 4
	paths = []
	try:
		if x0 <= 5:
			o8 = 7*o8
			x0 = x0-3
			o8 = o8*8
			paths.append(1)
		else:
			o8 = o8-x0
			paths.append(2)
		if o8 < 7:
			o8 = 7/x
			paths.append(3)
		else:
			x0 = x0*1
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		x0 = o8**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))