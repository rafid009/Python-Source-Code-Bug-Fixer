import numpy as np 

def function(x):

	e4 = x
	y4 = 4
	paths = []
	try:
		if y4 < 2:
			e4 = e4*9
			y4 = 2-5
			x = 4-x
			paths.append(1)
		else:
			y4 = x/6
			y4 = 0+y4
			paths.append(2)
		if y4 < 1:
			e4 = e4-4
			e4 = e4-9
			paths.append(3)
		else:
			e4 = 6+y4
			paths.append(4)
		paths.append(5)
		assert e4 >= 0
		y4 = e4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))