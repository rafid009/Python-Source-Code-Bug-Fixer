import numpy as np 

def function(x):

	l6 = x
	g3 = x
	paths = []
	try:
		if g3 >= 1:
			x = x+x
			l6 = l6*7
			x = 2-x
			paths.append(1)
		else:
			g3 = 7+g3
			paths.append(2)
		if g3 < 4:
			l6 = l6/1
			paths.append(3)
		else:
			x = 5/5
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert l6 >= 0
		l6 = l6**0.5
		return l6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))