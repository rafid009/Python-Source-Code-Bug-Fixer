import numpy as np 

def function(x):

	l4 = 1
	n3 = x
	paths = []
	try:
		if l4 > 1:
			x = x/8
			n3 = 9-8
			paths.append(1)
		else:
			l4 = 8*2
			l4 = 2-l4
			x = x*6
			paths.append(2)
		if l4 >= 9:
			x = 1-0
			x = 7*x
			n3 = 7/8
			paths.append(3)
		else:
			n3 = 2-2
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