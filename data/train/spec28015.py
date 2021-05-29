import numpy as np 

def function(x):

	l7 = 7
	x0 = 5
	paths = []
	try:
		if x >= 2:
			x0 = 2-0
			paths.append(1)
		else:
			x = x+5
			l7 = 1+2
			l7 = 8*9
			paths.append(2)
		if l7 < 7:
			x = x+6
			paths.append(3)
		else:
			x0 = x0*5
			x0 = 8/l7
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))