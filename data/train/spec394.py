import numpy as np 

def function(x):

	i4 = 9
	l8 = 2
	paths = []
	try:
		if x > 6:
			x = x/x
			x = 9/3
			paths.append(1)
		else:
			l8 = l8+7
			x = 8/8
			paths.append(2)
		if l8 > 2:
			x = 0*x
			paths.append(3)
		else:
			l8 = l8-x
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		l8 = l8**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))