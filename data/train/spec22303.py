import numpy as np 

def function(x):

	h9 = x
	l0 = 2
	paths = []
	try:
		if l0 < 8:
			x = 0+x
			paths.append(1)
		else:
			l0 = l0/h9
			paths.append(2)
		if h9 >= 2:
			l0 = 1*l0
			x = 9-3
			paths.append(3)
		else:
			h9 = h9/h9
			l0 = l0/5
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