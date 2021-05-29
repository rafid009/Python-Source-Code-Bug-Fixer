import numpy as np 

def function(x):

	l4 = x
	u7 = 5
	paths = []
	try:
		if l4 >= 0:
			l4 = l4+8
			paths.append(1)
		else:
			u7 = u7*5
			x = l4*x
			paths.append(2)
		if x > 9:
			u7 = 4+u7
			x = x*u7
			u7 = l4+8
			paths.append(3)
		else:
			u7 = u7-4
			u7 = u7/9
			u7 = u7-x
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