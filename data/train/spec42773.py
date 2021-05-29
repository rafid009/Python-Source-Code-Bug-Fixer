import numpy as np 

def function(x):

	u7 = x
	g3 = x
	paths = []
	try:
		if x <= 9:
			u7 = 4/u7
			paths.append(1)
		else:
			u7 = 8*x
			g3 = 3*9
			paths.append(2)
		if x <= 8:
			g3 = 1/g3
			u7 = u7-0
			paths.append(3)
		else:
			u7 = u7-g3
			u7 = 9-7
			u7 = g3/9
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		u7 = u7**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))