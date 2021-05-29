import numpy as np 

def function(x):

	h7 = x
	l4 = 2
	paths = []
	try:
		if h7 >= 4:
			x = x+3
			x = 8/2
			paths.append(1)
		else:
			x = 1*h7
			x = x/2
			h7 = h7/2
			paths.append(2)
		if h7 >= 1:
			x = 5-4
			x = x*9
			x = x/2
			paths.append(3)
		else:
			l4 = l4-x
			paths.append(4)
		paths.append(5)
		assert h7 >= 0
		l4 = h7**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))