import numpy as np 

def function(x):

	l4 = x
	a2 = 0
	paths = []
	try:
		if l4 <= 5:
			l4 = l4*l4
			x = 1*x
			paths.append(1)
		else:
			x = 1*x
			l4 = 5-l4
			paths.append(2)
		if a2 >= 7:
			x = 3-x
			x = a2+x
			paths.append(3)
		else:
			a2 = 6/l4
			l4 = l4*x
			x = 2+a2
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