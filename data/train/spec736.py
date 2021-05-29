import numpy as np 

def function(x):

	f7 = 8
	y2 = 5
	paths = []
	try:
		if f7 >= 2:
			y2 = y2+7
			f7 = 1-f7
			paths.append(1)
		else:
			x = 5-6
			paths.append(2)
		if x >= 1:
			x = y2-x
			paths.append(3)
		else:
			f7 = 7*x
			y2 = y2/y2
			y2 = y2-9
			paths.append(4)
		paths.append(5)
		assert f7 >= 0
		x = f7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))