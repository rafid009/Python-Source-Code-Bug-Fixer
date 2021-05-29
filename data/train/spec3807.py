import numpy as np 

def function(x):

	a7 = 8
	l0 = 4
	paths = []
	try:
		if x >= 6:
			l0 = l0+8
			x = 8/5
			paths.append(1)
		else:
			a7 = 7*2
			l0 = l0/l0
			paths.append(2)
		if x < 3:
			a7 = x/a7
			paths.append(3)
		else:
			x = x-a7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a7 = x**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))