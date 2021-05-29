import numpy as np 

def function(x):

	h2 = 6
	l0 = x
	x = x
	paths = []
	try:
		if h2 > 3:
			h2 = l0*6
			h2 = h2-9
			x = 9+x
			paths.append(1)
		else:
			l0 = l0/8
			l0 = h2/9
			h2 = 2/l0
			paths.append(2)
		if x > 8:
			l0 = l0*6
			paths.append(3)
		else:
			l0 = x+8
			h2 = h2/1
			l0 = l0+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		h2 = x**0.5
		return h2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))