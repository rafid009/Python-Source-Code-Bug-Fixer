import numpy as np 

def function(x):

	l6 = x
	g5 = 2
	paths = []
	try:
		if g5 < 8:
			x = 6/4
			g5 = 6-g5
			paths.append(1)
		else:
			l6 = l6+7
			x = x+5
			g5 = g5/x
			paths.append(2)
		if l6 < 3:
			l6 = l6/7
			paths.append(3)
		else:
			l6 = x/l6
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