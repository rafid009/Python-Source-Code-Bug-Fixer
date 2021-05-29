import numpy as np 

def function(x):

	l4 = x
	p2 = 4
	x = 3
	paths = []
	try:
		if p2 >= 8:
			x = l4*5
			x = x*l4
			paths.append(1)
		else:
			p2 = p2*p2
			p2 = p2+p2
			paths.append(2)
		if x >= 4:
			x = 1-l4
			p2 = 0-l4
			paths.append(3)
		else:
			x = 8*x
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