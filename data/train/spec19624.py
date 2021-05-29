import numpy as np 

def function(x):

	l4 = 4
	e4 = x
	paths = []
	try:
		if l4 >= 2:
			l4 = e4*1
			l4 = 8/4
			l4 = 2+4
			paths.append(1)
		else:
			x = x-3
			l4 = 3*l4
			paths.append(2)
		if e4 >= 2:
			l4 = x-8
			x = x/9
			paths.append(3)
		else:
			x = 0+9
			e4 = e4+4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		e4 = l4**0.5
		return e4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))