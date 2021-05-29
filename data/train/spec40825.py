import numpy as np 

def function(x):

	l4 = x
	n2 = x
	paths = []
	try:
		if x >= 4:
			x = 0-4
			l4 = x/7
			paths.append(1)
		else:
			n2 = l4*5
			paths.append(2)
		if x >= 4:
			l4 = 2/l4
			x = x-3
			x = 0+x
			paths.append(3)
		else:
			x = x/8
			n2 = n2/1
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