import numpy as np 

def function(x):

	y2 = 9
	y4 = x
	x = 8
	paths = []
	try:
		if y4 <= 1:
			y2 = 8+y2
			paths.append(1)
		else:
			x = y2-8
			x = x+7
			paths.append(2)
		if y2 <= 8:
			y4 = x/8
			x = x-y4
			paths.append(3)
		else:
			x = x*5
			x = 5-x
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