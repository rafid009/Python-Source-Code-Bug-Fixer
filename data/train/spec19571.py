import numpy as np 

def function(x):

	g9 = 1
	l3 = 3
	paths = []
	try:
		if g9 > 2:
			g9 = g9/l3
			paths.append(1)
		else:
			l3 = 2-x
			paths.append(2)
		if g9 >= 5:
			l3 = 3*l3
			x = x*6
			g9 = x/5
			paths.append(3)
		else:
			g9 = g9+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l3 = x**0.5
		return l3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))