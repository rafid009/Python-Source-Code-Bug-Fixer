import numpy as np 

def function(x):

	l2 = x
	p4 = 6
	x = 2
	paths = []
	try:
		if l2 > 5:
			x = x+l2
			x = x-x
			p4 = 2+p4
			paths.append(1)
		else:
			x = p4*x
			l2 = l2-2
			paths.append(2)
		if l2 < 0:
			x = 4+x
			paths.append(3)
		else:
			x = x*3
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