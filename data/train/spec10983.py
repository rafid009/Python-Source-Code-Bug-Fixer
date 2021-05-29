import numpy as np 

def function(x):

	l2 = x
	n1 = x
	paths = []
	try:
		if l2 <= 5:
			l2 = l2-3
			paths.append(1)
		else:
			l2 = 4+l2
			paths.append(2)
		if n1 < 6:
			l2 = l2/3
			x = l2*x
			paths.append(3)
		else:
			n1 = n1-l2
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))