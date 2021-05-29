import numpy as np 

def function(x):

	v4 = x
	l4 = 0
	paths = []
	try:
		if x <= 5:
			l4 = x-l4
			paths.append(1)
		else:
			l4 = l4/3
			paths.append(2)
		if x >= 7:
			x = 7-x
			x = x+x
			l4 = l4*2
			paths.append(3)
		else:
			v4 = 4/v4
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