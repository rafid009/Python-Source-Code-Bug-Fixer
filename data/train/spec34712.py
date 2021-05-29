import numpy as np 

def function(x):

	y4 = 8
	y3 = x
	paths = []
	try:
		if y4 <= 9:
			x = 7-x
			paths.append(1)
		else:
			x = x+y4
			paths.append(2)
		if y3 < 3:
			y4 = 7+9
			y4 = y4*6
			paths.append(3)
		else:
			y3 = 9/x
			y4 = y4*y3
			x = x/4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y3 = y4**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))