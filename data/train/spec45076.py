import numpy as np 

def function(x):

	l4 = 7
	h4 = 5
	paths = []
	try:
		if h4 <= 8:
			h4 = h4-4
			h4 = 9-h4
			h4 = h4+7
			paths.append(1)
		else:
			l4 = l4+8
			l4 = h4+l4
			h4 = h4-0
			paths.append(2)
		if l4 > 4:
			x = x/7
			h4 = h4+2
			paths.append(3)
		else:
			h4 = 2/l4
			l4 = 3*9
			h4 = 9/l4
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