import numpy as np 

def function(x):

	d7 = x
	x9 = 8
	paths = []
	try:
		if d7 >= 3:
			x = 8/6
			x9 = x9/8
			paths.append(1)
		else:
			x9 = 4/9
			x = x-8
			paths.append(2)
		if x9 < 7:
			x9 = 5-x
			paths.append(3)
		else:
			d7 = d7/6
			d7 = 0-d7
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x9 = d7**0.5
		return x9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))