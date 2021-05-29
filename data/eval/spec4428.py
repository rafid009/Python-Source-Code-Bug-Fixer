import numpy as np 

def function(x):

	y1 = 8
	y7 = x
	paths = []
	try:
		if y7 < 3:
			y7 = 5/y7
			y1 = y1/3
			x = 9/9
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if y7 < 4:
			y1 = y1-x
			y7 = 4+0
			paths.append(3)
		else:
			y1 = 3-y1
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