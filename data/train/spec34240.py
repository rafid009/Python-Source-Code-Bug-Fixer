import numpy as np 

def function(x):

	g9 = 1
	l2 = 5
	paths = []
	try:
		if l2 > 6:
			l2 = 0*3
			l2 = 0*l2
			paths.append(1)
		else:
			l2 = 9-l2
			paths.append(2)
		if g9 >= 4:
			g9 = 8-g9
			paths.append(3)
		else:
			l2 = 1-x
			g9 = x+8
			paths.append(4)
		paths.append(5)
		assert l2 >= 0
		x = l2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))