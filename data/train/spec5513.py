import numpy as np 

def function(x):

	l0 = 0
	b1 = 4
	paths = []
	try:
		if x < 8:
			b1 = l0*b1
			l0 = 9-b1
			paths.append(1)
		else:
			l0 = x-l0
			paths.append(2)
		if b1 < 0:
			l0 = l0*2
			l0 = l0+4
			paths.append(3)
		else:
			l0 = l0+l0
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