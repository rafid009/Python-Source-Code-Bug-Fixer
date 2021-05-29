import numpy as np 

def function(x):

	l4 = x
	h6 = 7
	paths = []
	try:
		if h6 < 7:
			x = l4/l4
			paths.append(1)
		else:
			l4 = x+l4
			paths.append(2)
		if l4 > 9:
			x = x-3
			l4 = 7*l4
			x = 1*9
			paths.append(3)
		else:
			l4 = l4/6
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))