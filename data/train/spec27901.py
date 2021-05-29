import numpy as np 

def function(x):

	l4 = x
	h1 = 4
	paths = []
	try:
		if x < 1:
			l4 = l4/4
			x = x-4
			l4 = l4*6
			paths.append(1)
		else:
			l4 = l4+8
			h1 = 5/h1
			paths.append(2)
		if l4 >= 0:
			l4 = 6+l4
			l4 = x+6
			l4 = 8*h1
			paths.append(3)
		else:
			x = 8+x
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