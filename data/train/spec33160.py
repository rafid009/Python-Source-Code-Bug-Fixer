import numpy as np 

def function(x):

	u5 = x
	g7 = 4
	paths = []
	try:
		if u5 >= 0:
			u5 = u5*6
			x = 5+x
			paths.append(1)
		else:
			u5 = u5*1
			u5 = u5+3
			x = x-g7
			paths.append(2)
		if x > 0:
			u5 = 6+7
			x = g7*5
			u5 = 7/u5
			paths.append(3)
		else:
			g7 = g7/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))