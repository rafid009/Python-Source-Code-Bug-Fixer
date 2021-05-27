import numpy as np 

def function(x):

	l4 = 6
	p6 = 3
	paths = []
	try:
		if l4 <= 5:
			p6 = 9-3
			paths.append(1)
		else:
			l4 = 0+4
			x = 6/x
			x = x*p6
			paths.append(2)
		if x < 0:
			p6 = p6/p6
			paths.append(3)
		else:
			p6 = p6-p6
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