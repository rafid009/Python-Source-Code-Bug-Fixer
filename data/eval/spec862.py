import numpy as np 

def function(x):

	l0 = 7
	b8 = 7
	paths = []
	try:
		if b8 < 9:
			l0 = 2/l0
			paths.append(1)
		else:
			x = x+8
			x = 3/6
			paths.append(2)
		if b8 <= 5:
			l0 = b8+l0
			b8 = l0-4
			paths.append(3)
		else:
			b8 = x-b8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l0 = x**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))