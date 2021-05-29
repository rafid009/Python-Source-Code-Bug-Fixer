import numpy as np 

def function(x):

	l4 = x
	h1 = 1
	paths = []
	try:
		if h1 >= 7:
			x = 1*x
			h1 = l4-l4
			paths.append(1)
		else:
			l4 = l4+6
			h1 = 7*7
			l4 = 9+l4
			paths.append(2)
		if l4 <= 8:
			x = 4-x
			h1 = h1*5
			paths.append(3)
		else:
			x = x-1
			l4 = x+x
			h1 = h1+3
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