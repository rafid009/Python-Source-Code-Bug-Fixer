import numpy as np 

def function(x):

	n3 = x
	l2 = 6
	paths = []
	try:
		if x <= 4:
			n3 = n3*7
			l2 = l2*n3
			paths.append(1)
		else:
			l2 = 3*6
			paths.append(2)
		if l2 > 1:
			x = 8*x
			l2 = l2-2
			l2 = 5/8
			paths.append(3)
		else:
			l2 = 2-3
			n3 = x/9
			paths.append(4)
		paths.append(5)
		assert n3 >= 0
		x = n3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))