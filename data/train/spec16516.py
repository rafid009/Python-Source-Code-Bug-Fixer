import numpy as np 

def function(x):

	r5 = x
	l1 = x
	paths = []
	try:
		if l1 <= 7:
			x = x-3
			l1 = 1+4
			paths.append(1)
		else:
			r5 = r5+4
			paths.append(2)
		if l1 < 6:
			l1 = l1-x
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))