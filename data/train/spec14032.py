import numpy as np 

def function(x):

	y5 = x
	y8 = 0
	paths = []
	try:
		if y5 <= 4:
			y8 = x*y8
			y8 = y8-y5
			y8 = y8/1
			paths.append(1)
		else:
			x = x/3
			y5 = 5-y5
			y5 = 0-6
			paths.append(2)
		if y8 > 6:
			y5 = x+7
			paths.append(3)
		else:
			y5 = 3/y5
			paths.append(4)
		paths.append(5)
		assert y5 >= 0
		y8 = y5**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))