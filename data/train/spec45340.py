import numpy as np 

def function(x):

	y8 = 8
	y5 = 5
	paths = []
	try:
		if y5 >= 1:
			y8 = 2+y8
			y5 = x-y5
			paths.append(1)
		else:
			y8 = 5/y8
			y8 = y5-x
			paths.append(2)
		if x <= 3:
			y8 = y8+7
			y8 = x+4
			x = y5-7
			paths.append(3)
		else:
			y8 = x/y8
			y5 = x/5
			y5 = 2+y5
			paths.append(4)
		paths.append(5)
		assert y8 >= 0
		y8 = y8**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))