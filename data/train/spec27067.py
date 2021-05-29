import numpy as np 

def function(x):

	l0 = x
	e9 = x
	x = 7
	paths = []
	try:
		if l0 <= 0:
			e9 = e9*e9
			x = 8*e9
			x = e9*4
			paths.append(1)
		else:
			l0 = 8-e9
			paths.append(2)
		if e9 < 6:
			l0 = l0*e9
			paths.append(3)
		else:
			x = 1-x
			e9 = 0*8
			x = 6-9
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