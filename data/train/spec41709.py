import numpy as np 

def function(x):

	e0 = 1
	l0 = 9
	paths = []
	try:
		if x >= 0:
			e0 = e0-e0
			e0 = e0*e0
			e0 = e0*6
			paths.append(1)
		else:
			e0 = x+e0
			l0 = 4-5
			paths.append(2)
		if l0 < 0:
			x = x/4
			l0 = x/4
			l0 = l0-4
			paths.append(3)
		else:
			l0 = 3*1
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))