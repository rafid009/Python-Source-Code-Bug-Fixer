import numpy as np 

def function(x):

	l1 = 1
	u7 = x
	paths = []
	try:
		if l1 >= 2:
			l1 = l1-6
			l1 = l1+l1
			paths.append(1)
		else:
			u7 = x-u7
			x = l1-7
			paths.append(2)
		if l1 >= 3:
			l1 = 1-l1
			u7 = 4-6
			paths.append(3)
		else:
			l1 = l1-9
			u7 = 9-u7
			u7 = l1/u7
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