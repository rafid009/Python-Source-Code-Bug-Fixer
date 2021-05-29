import numpy as np 

def function(x):

	p4 = x
	l0 = x
	paths = []
	try:
		if x >= 6:
			l0 = 1+p4
			p4 = 8/4
			paths.append(1)
		else:
			l0 = 2-l0
			paths.append(2)
		if p4 < 7:
			p4 = p4/p4
			paths.append(3)
		else:
			x = x-8
			paths.append(4)
		paths.append(5)
		assert l0 >= 0
		l0 = l0**0.5
		return l0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))