import numpy as np 

def function(x):

	l4 = x
	x0 = 8
	paths = []
	try:
		if l4 >= 7:
			x0 = x+7
			l4 = 6+l4
			paths.append(1)
		else:
			x = l4+x
			x = x0+x
			paths.append(2)
		if x0 >= 2:
			x0 = x0/2
			x = x*x
			l4 = l4/4
			paths.append(3)
		else:
			x = l4-l4
			l4 = 0*l4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		x0 = l4**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))