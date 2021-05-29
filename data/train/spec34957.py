import numpy as np 

def function(x):

	g3 = x
	l4 = x
	x = x
	paths = []
	try:
		if l4 > 8:
			l4 = 9*l4
			paths.append(1)
		else:
			g3 = l4*7
			paths.append(2)
		if l4 <= 6:
			l4 = l4*8
			g3 = x+7
			x = 5*x
			paths.append(3)
		else:
			g3 = 8*l4
			x = 3-3
			l4 = l4/l4
			paths.append(4)
		paths.append(5)
		assert l4 >= 0
		l4 = l4**0.5
		return l4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))