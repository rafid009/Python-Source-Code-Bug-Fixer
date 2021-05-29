import numpy as np 

def function(x):

	h2 = 5
	u7 = 0
	paths = []
	try:
		if x < 8:
			u7 = x-u7
			x = 4-x
			u7 = u7/6
			paths.append(1)
		else:
			u7 = 5+7
			paths.append(2)
		if x >= 9:
			u7 = 7/h2
			x = u7-x
			u7 = 5+x
			paths.append(3)
		else:
			u7 = h2/2
			paths.append(4)
		paths.append(5)
		assert u7 >= 0
		x = u7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))