import numpy as np 

def function(x):

	u5 = x
	x5 = x
	x = x
	paths = []
	try:
		if x >= 2:
			x = u5*9
			u5 = u5+7
			x5 = 1-x5
			paths.append(1)
		else:
			x = x+x
			paths.append(2)
		if x5 >= 5:
			x5 = 5-2
			paths.append(3)
		else:
			u5 = x5/u5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))