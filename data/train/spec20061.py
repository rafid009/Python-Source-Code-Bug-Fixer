import numpy as np 

def function(x):

	l5 = x
	l8 = 0
	paths = []
	try:
		if l5 >= 2:
			l5 = 1/l5
			paths.append(1)
		else:
			x = 8-4
			paths.append(2)
		if l8 <= 0:
			l8 = 2*l5
			x = 1*x
			l5 = 7/l5
			paths.append(3)
		else:
			l5 = 0/7
			x = 9-4
			l8 = 1/l8
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