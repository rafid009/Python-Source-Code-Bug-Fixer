import numpy as np 

def function(x):

	y1 = 7
	paths = []
	try:
		if x <= 4:
			y1 = 9/x
			x = x+3
			y1 = 9/5
			paths.append(1)
		else:
			x = y1-1
			y1 = 7-6
			y1 = y1/4
			paths.append(2)
		if y1 >= 9:
			x = 2-2
			paths.append(3)
		else:
			x = y1/x
			y1 = x/y1
			y1 = y1/4
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))