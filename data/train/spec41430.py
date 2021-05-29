import numpy as np 

def function(x):

	e3 = 2
	l2 = x
	paths = []
	try:
		if l2 >= 0:
			e3 = e3-4
			x = x*9
			paths.append(1)
		else:
			e3 = e3+1
			x = 3+0
			e3 = e3+8
			paths.append(2)
		if x <= 3:
			e3 = 0-9
			x = x-4
			paths.append(3)
		else:
			x = 9-4
			x = 3-3
			l2 = 1*l2
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		l2 = l2**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))