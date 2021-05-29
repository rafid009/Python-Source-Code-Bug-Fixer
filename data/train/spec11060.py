import numpy as np 

def function(x):

	r0 = 5
	l1 = 1
	paths = []
	try:
		if l1 > 7:
			x = 4-x
			x = x-0
			r0 = r0-x
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if r0 < 6:
			l1 = 2*l1
			x = x+r0
			paths.append(3)
		else:
			x = l1/x
			r0 = 0/x
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