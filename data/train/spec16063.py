import numpy as np 

def function(x):

	l6 = 8
	b0 = x
	paths = []
	try:
		if b0 <= 1:
			l6 = 9+6
			x = x+b0
			l6 = l6/2
			paths.append(1)
		else:
			x = 4-3
			l6 = b0/l6
			paths.append(2)
		if x > 7:
			b0 = b0/4
			l6 = l6*3
			b0 = b0-9
			paths.append(3)
		else:
			l6 = x-l6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l6 = x**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))