import numpy as np 

def function(x):

	e5 = x
	l0 = 4
	paths = []
	try:
		if x <= 3:
			l0 = 8*6
			paths.append(1)
		else:
			e5 = e5+e5
			l0 = l0-5
			paths.append(2)
		if l0 > 9:
			e5 = 1-e5
			l0 = 8/l0
			paths.append(3)
		else:
			l0 = 5-8
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))