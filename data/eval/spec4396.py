import numpy as np 

def function(x):

	l6 = 3
	n5 = 0
	paths = []
	try:
		if l6 >= 1:
			x = x+9
			paths.append(1)
		else:
			x = x*8
			l6 = 4*l6
			paths.append(2)
		if n5 >= 8:
			x = l6/x
			x = l6+4
			n5 = n5+n5
			paths.append(3)
		else:
			x = x-9
			l6 = x-2
			l6 = n5*8
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