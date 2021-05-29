import numpy as np 

def function(x):

	b7 = x
	l8 = 0
	paths = []
	try:
		if l8 >= 4:
			x = x*9
			paths.append(1)
		else:
			b7 = 5/b7
			b7 = b7/4
			b7 = b7*5
			paths.append(2)
		if x >= 3:
			l8 = 2-6
			x = b7-b7
			paths.append(3)
		else:
			l8 = x/b7
			x = x/x
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		l8 = b7**0.5
		return l8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))