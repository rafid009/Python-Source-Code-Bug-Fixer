import numpy as np 

def function(x):

	u5 = 6
	x8 = 9
	paths = []
	try:
		if x <= 3:
			x8 = x+x8
			x = 8/x
			paths.append(1)
		else:
			u5 = u5-2
			u5 = x-3
			u5 = u5+7
			paths.append(2)
		if x8 < 6:
			x8 = x8-u5
			u5 = x8-8
			x = 9-x
			paths.append(3)
		else:
			x = x*4
			u5 = 9*x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x8 = x8**0.5
		return x8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))