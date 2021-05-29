import numpy as np 

def function(x):

	h0 = 7
	l2 = x
	paths = []
	try:
		if l2 >= 9:
			h0 = l2-l2
			x = 3+x
			paths.append(1)
		else:
			h0 = h0*6
			paths.append(2)
		if x > 1:
			l2 = h0*l2
			h0 = h0+9
			paths.append(3)
		else:
			h0 = x-4
			h0 = 3-0
			l2 = 1+l2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))