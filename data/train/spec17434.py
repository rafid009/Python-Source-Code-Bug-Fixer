import numpy as np 

def function(x):

	h6 = x
	l2 = 1
	paths = []
	try:
		if h6 >= 3:
			l2 = l2*0
			l2 = l2*9
			paths.append(1)
		else:
			l2 = l2-7
			h6 = 5-7
			paths.append(2)
		if l2 > 6:
			x = x/x
			paths.append(3)
		else:
			x = 9*l2
			h6 = 2-l2
			h6 = h6-2
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