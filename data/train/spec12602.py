import numpy as np 

def function(x):

	l7 = 0
	h3 = 8
	paths = []
	try:
		if x < 7:
			l7 = 9*l7
			paths.append(1)
		else:
			h3 = h3+h3
			l7 = 4+l7
			paths.append(2)
		if h3 > 8:
			x = l7*l7
			paths.append(3)
		else:
			h3 = 3+2
			l7 = l7+x
			h3 = h3*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))