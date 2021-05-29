import numpy as np 

def function(x):

	y7 = 8
	d9 = x
	paths = []
	try:
		if d9 <= 9:
			x = 2-x
			paths.append(1)
		else:
			y7 = x/y7
			y7 = y7*6
			d9 = 0+2
			paths.append(2)
		if x < 1:
			y7 = y7*3
			paths.append(3)
		else:
			x = x*x
			d9 = d9-x
			y7 = y7-y7
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		y7 = d9**0.5
		return y7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))