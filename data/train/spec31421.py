import numpy as np 

def function(x):

	y7 = 2
	u7 = 5
	paths = []
	try:
		if u7 < 2:
			u7 = y7/y7
			u7 = u7*1
			paths.append(1)
		else:
			y7 = y7*3
			x = x/4
			paths.append(2)
		if u7 > 4:
			y7 = y7/3
			u7 = 6*x
			u7 = u7/3
			paths.append(3)
		else:
			y7 = y7-6
			y7 = u7*y7
			y7 = y7*7
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