import numpy as np 

def function(x):

	y8 = 8
	o5 = 0
	paths = []
	try:
		if x < 0:
			y8 = 0-o5
			paths.append(1)
		else:
			o5 = o5-4
			y8 = y8-2
			o5 = o5-6
			paths.append(2)
		if x < 9:
			o5 = y8/1
			paths.append(3)
		else:
			y8 = 9*1
			x = x-6
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		y8 = o5**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))