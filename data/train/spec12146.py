import numpy as np 

def function(x):

	p1 = 6
	l2 = 1
	paths = []
	try:
		if l2 >= 3:
			p1 = 6*l2
			paths.append(1)
		else:
			l2 = x-6
			l2 = 5+l2
			l2 = 5-7
			paths.append(2)
		if x > 6:
			p1 = 3-7
			p1 = 9/x
			paths.append(3)
		else:
			l2 = l2-7
			p1 = l2/p1
			p1 = p1/1
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