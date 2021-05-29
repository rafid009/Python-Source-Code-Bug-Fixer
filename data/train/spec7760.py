import numpy as np 

def function(x):

	d7 = x
	y7 = 3
	paths = []
	try:
		if y7 > 3:
			d7 = y7+0
			y7 = 6+y7
			paths.append(1)
		else:
			x = d7*6
			paths.append(2)
		if y7 < 7:
			y7 = 9*y7
			d7 = d7/7
			x = y7+4
			paths.append(3)
		else:
			y7 = y7*3
			x = 5+x
			y7 = 3*5
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