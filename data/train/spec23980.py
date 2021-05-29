import numpy as np 

def function(x):

	l2 = x
	n5 = x
	paths = []
	try:
		if n5 <= 9:
			l2 = x+x
			x = x-4
			l2 = l2*l2
			paths.append(1)
		else:
			x = 3+1
			paths.append(2)
		if x <= 6:
			n5 = n5*5
			n5 = l2/2
			x = x-6
			paths.append(3)
		else:
			x = n5+l2
			n5 = 7*n5
			n5 = n5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))