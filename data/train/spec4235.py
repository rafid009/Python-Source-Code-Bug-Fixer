import numpy as np 

def function(x):

	u7 = 8
	n6 = 5
	x = 2
	paths = []
	try:
		if x > 9:
			n6 = x/n6
			u7 = 4+u7
			paths.append(1)
		else:
			n6 = x+n6
			u7 = u7-u7
			u7 = u7-1
			paths.append(2)
		if n6 > 0:
			x = x+0
			paths.append(3)
		else:
			x = n6-2
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