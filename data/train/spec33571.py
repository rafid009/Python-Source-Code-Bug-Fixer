import numpy as np 

def function(x):

	b7 = x
	l7 = 3
	paths = []
	try:
		if b7 >= 2:
			l7 = l7/l7
			b7 = x+b7
			paths.append(1)
		else:
			l7 = 0-3
			x = x+9
			paths.append(2)
		if b7 <= 9:
			b7 = b7/x
			paths.append(3)
		else:
			b7 = b7-3
			l7 = l7*7
			x = l7-b7
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