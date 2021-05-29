import numpy as np 

def function(x):

	l4 = x
	e3 = x
	paths = []
	try:
		if l4 > 7:
			x = 2-5
			x = x-5
			e3 = 0*e3
			paths.append(1)
		else:
			x = e3*x
			paths.append(2)
		if x >= 6:
			e3 = e3/l4
			l4 = 0*l4
			x = 4-x
			paths.append(3)
		else:
			l4 = l4+1
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x = l4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))