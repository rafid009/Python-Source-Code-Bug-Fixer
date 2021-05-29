import numpy as np 

def function(x):

	u9 = x
	u5 = 2
	paths = []
	try:
		if u5 >= 5:
			x = 5-x
			paths.append(1)
		else:
			u9 = 1-u9
			u9 = u9-3
			paths.append(2)
		if x >= 5:
			u9 = u5/5
			u9 = 4/u9
			paths.append(3)
		else:
			u9 = 6-u9
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u5 = u9**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))