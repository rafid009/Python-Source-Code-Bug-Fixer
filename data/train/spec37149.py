import numpy as np 

def function(x):

	f3 = 0
	u7 = x
	paths = []
	try:
		if x >= 1:
			u7 = u7/7
			f3 = f3/x
			paths.append(1)
		else:
			x = 4+x
			paths.append(2)
		if u7 < 0:
			f3 = f3-8
			paths.append(3)
		else:
			f3 = 3-2
			u7 = u7-1
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