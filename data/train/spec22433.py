import numpy as np 

def function(x):

	o5 = x
	l8 = x
	paths = []
	try:
		if x >= 4:
			x = x-7
			paths.append(1)
		else:
			l8 = 0/l8
			paths.append(2)
		if x <= 1:
			l8 = l8+8
			paths.append(3)
		else:
			x = 4+o5
			paths.append(4)
		paths.append(5)
		assert o5 >= 0
		l8 = o5**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))