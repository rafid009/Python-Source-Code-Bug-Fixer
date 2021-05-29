import numpy as np 

def function(x):

	y8 = x
	d2 = x
	paths = []
	try:
		if y8 < 2:
			y8 = y8+y8
			paths.append(1)
		else:
			y8 = y8/4
			paths.append(2)
		if x <= 2:
			d2 = x+8
			y8 = y8*3
			paths.append(3)
		else:
			d2 = d2/7
			d2 = d2+y8
			x = x/y8
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))