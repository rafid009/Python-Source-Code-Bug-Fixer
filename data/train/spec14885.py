import numpy as np 

def function(x):

	d7 = x
	y5 = x
	paths = []
	try:
		if y5 < 1:
			y5 = 0-y5
			d7 = d7*1
			paths.append(1)
		else:
			d7 = d7/d7
			paths.append(2)
		if d7 > 4:
			d7 = 1/d7
			d7 = y5+7
			paths.append(3)
		else:
			y5 = 5-x
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		x = d7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))