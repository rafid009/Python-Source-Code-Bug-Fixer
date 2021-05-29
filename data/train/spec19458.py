import numpy as np 

def function(x):

	p1 = 8
	l2 = x
	paths = []
	try:
		if x <= 1:
			p1 = p1-x
			l2 = l2-x
			paths.append(1)
		else:
			l2 = x-x
			paths.append(2)
		if p1 > 5:
			p1 = 0+9
			paths.append(3)
		else:
			l2 = x/l2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l2 = x**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))