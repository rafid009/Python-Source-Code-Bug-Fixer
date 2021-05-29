import numpy as np 

def function(x):

	g2 = 2
	l2 = x
	paths = []
	try:
		if l2 <= 6:
			l2 = g2-x
			x = 9*x
			l2 = x/l2
			paths.append(1)
		else:
			x = x+7
			paths.append(2)
		if g2 > 2:
			x = 5/l2
			paths.append(3)
		else:
			x = x+1
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