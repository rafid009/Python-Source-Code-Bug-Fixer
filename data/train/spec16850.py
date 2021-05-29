import numpy as np 

def function(x):

	y4 = 7
	y2 = 8
	paths = []
	try:
		if y2 > 5:
			y2 = 8/x
			y4 = x-y2
			x = 3-x
			paths.append(1)
		else:
			x = 7+x
			y4 = y4-5
			y4 = y4+y4
			paths.append(2)
		if y4 >= 7:
			y4 = 7-y2
			y2 = y2+5
			paths.append(3)
		else:
			y2 = 5-5
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