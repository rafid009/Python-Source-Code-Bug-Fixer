import numpy as np 

def function(x):

	l4 = x
	e1 = x
	paths = []
	try:
		if e1 <= 2:
			l4 = l4*4
			paths.append(1)
		else:
			l4 = e1*7
			paths.append(2)
		if x > 0:
			l4 = l4-6
			l4 = l4-4
			x = 2/x
			paths.append(3)
		else:
			l4 = 3+x
			e1 = l4-e1
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