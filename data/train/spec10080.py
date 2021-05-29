import numpy as np 

def function(x):

	a9 = 1
	l5 = x
	x = 3
	paths = []
	try:
		if a9 >= 7:
			l5 = l5-0
			paths.append(1)
		else:
			x = x*a9
			x = x-l5
			x = x+3
			paths.append(2)
		if a9 >= 2:
			l5 = 7/x
			paths.append(3)
		else:
			l5 = a9/3
			a9 = a9-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l5 = x**0.5
		return l5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))