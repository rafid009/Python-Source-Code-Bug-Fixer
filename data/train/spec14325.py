import numpy as np 

def function(x):

	l0 = 9
	p7 = x
	paths = []
	try:
		if p7 >= 6:
			p7 = 9*p7
			paths.append(1)
		else:
			l0 = 2-l0
			x = 9+x
			p7 = p7*4
			paths.append(2)
		if x > 2:
			x = 6*x
			l0 = l0/4
			paths.append(3)
		else:
			x = p7-x
			x = 9/x
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		x = l0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))