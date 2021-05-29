import numpy as np 

def function(x):

	d7 = x
	y8 = 8
	paths = []
	try:
		if x <= 6:
			d7 = d7*8
			paths.append(1)
		else:
			d7 = 1/y8
			d7 = d7*4
			d7 = 7-d7
			paths.append(2)
		if x < 6:
			y8 = y8-6
			d7 = d7/2
			paths.append(3)
		else:
			y8 = 5/6
			d7 = 8/9
			y8 = y8-y8
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		y8 = d7**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))