import numpy as np 

def function(x):

	l6 = 5
	s2 = 6
	paths = []
	try:
		if s2 >= 7:
			l6 = l6/4
			paths.append(1)
		else:
			l6 = l6-9
			l6 = 1-7
			x = x/2
			paths.append(2)
		if s2 < 5:
			x = 8-9
			paths.append(3)
		else:
			l6 = 2+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))