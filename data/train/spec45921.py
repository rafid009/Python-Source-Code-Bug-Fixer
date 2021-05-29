import numpy as np 

def function(x):

	l4 = x
	m4 = x
	paths = []
	try:
		if l4 <= 8:
			m4 = 2-3
			l4 = 8-8
			x = 1-3
			paths.append(1)
		else:
			x = 9/x
			paths.append(2)
		if l4 <= 0:
			l4 = l4*3
			l4 = 5-m4
			m4 = 6*4
			paths.append(3)
		else:
			x = 6/l4
			l4 = 1+l4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l4 = x**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))