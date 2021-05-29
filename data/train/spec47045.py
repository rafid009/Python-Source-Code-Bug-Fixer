import numpy as np 

def function(x):

	u7 = x
	j4 = 8
	paths = []
	try:
		if x > 3:
			u7 = u7+0
			paths.append(1)
		else:
			x = 0*5
			u7 = u7*x
			paths.append(2)
		if x >= 0:
			u7 = 5-u7
			u7 = 9/u7
			j4 = 4/j4
			paths.append(3)
		else:
			j4 = x-1
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