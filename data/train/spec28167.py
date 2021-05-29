import numpy as np 

def function(x):

	v0 = 6
	y4 = x
	paths = []
	try:
		if y4 >= 9:
			v0 = v0-8
			paths.append(1)
		else:
			y4 = 2-y4
			x = y4-9
			paths.append(2)
		if v0 <= 6:
			x = x+6
			x = x/7
			y4 = y4/x
			paths.append(3)
		else:
			y4 = y4*y4
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))