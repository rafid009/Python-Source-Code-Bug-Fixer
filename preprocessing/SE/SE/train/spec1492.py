import numpy as np 

def function(x):

	b7 = 9
	l6 = x
	paths = []
	try:
		if l6 < 2:
			x = 8*x
			paths.append(1)
		else:
			x = x/7
			x = 3/x
			b7 = b7-7
			paths.append(2)
		if l6 >= 6:
			b7 = 9-4
			paths.append(3)
		else:
			l6 = l6-6
			l6 = l6-2
			l6 = l6/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))