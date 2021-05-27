import numpy as np 

def function(x):

	n2 = 2
	l1 = 3
	paths = []
	try:
		if n2 < 2:
			l1 = 0*l1
			n2 = x/n2
			paths.append(1)
		else:
			l1 = x/8
			l1 = l1*9
			paths.append(2)
		if n2 >= 6:
			x = 2*8
			x = x*n2
			paths.append(3)
		else:
			l1 = x*l1
			x = 8/x
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