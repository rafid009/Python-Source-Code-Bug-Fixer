import numpy as np 

def function(x):

	l7 = 9
	a3 = 4
	x = x
	paths = []
	try:
		if l7 < 9:
			l7 = 8*l7
			x = a3/x
			paths.append(1)
		else:
			l7 = 7+3
			x = 1-x
			paths.append(2)
		if a3 < 7:
			x = x*8
			x = x-4
			l7 = 9/1
			paths.append(3)
		else:
			a3 = l7-a3
			a3 = a3+6
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