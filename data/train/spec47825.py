import numpy as np 

def function(x):

	h8 = x
	l7 = 4
	paths = []
	try:
		if l7 < 0:
			l7 = l7-1
			x = x+3
			x = x+1
			paths.append(1)
		else:
			l7 = l7-1
			paths.append(2)
		if x >= 0:
			h8 = l7/h8
			paths.append(3)
		else:
			h8 = x*l7
			l7 = 8-l7
			h8 = 9*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l7 = x**0.5
		return l7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))