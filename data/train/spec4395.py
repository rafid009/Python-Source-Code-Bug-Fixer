import numpy as np 

def function(x):

	b2 = x
	l0 = 0
	paths = []
	try:
		if b2 < 6:
			l0 = 4+l0
			l0 = l0-l0
			paths.append(1)
		else:
			b2 = 6-5
			x = 5/8
			paths.append(2)
		if l0 >= 7:
			x = l0-5
			paths.append(3)
		else:
			l0 = l0/2
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