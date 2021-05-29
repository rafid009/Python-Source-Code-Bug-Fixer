import numpy as np 

def function(x):

	l6 = x
	n2 = 6
	paths = []
	try:
		if n2 > 8:
			n2 = n2/x
			paths.append(1)
		else:
			l6 = 4+l6
			l6 = l6-5
			paths.append(2)
		if n2 >= 2:
			n2 = 7+5
			n2 = x+n2
			paths.append(3)
		else:
			n2 = 3*n2
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		x = l6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))