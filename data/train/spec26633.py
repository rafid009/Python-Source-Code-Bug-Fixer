import numpy as np 

def function(x):

	u2 = x
	l1 = 2
	paths = []
	try:
		if l1 > 8:
			l1 = l1-1
			x = 9*x
			paths.append(1)
		else:
			u2 = 5+4
			x = 9/x
			paths.append(2)
		if x >= 7:
			l1 = l1*5
			paths.append(3)
		else:
			l1 = u2-x
			x = x-8
			x = x+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u2 = x**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))