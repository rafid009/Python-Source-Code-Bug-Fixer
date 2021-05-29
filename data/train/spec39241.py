import numpy as np 

def function(x):

	l5 = 3
	g5 = 7
	paths = []
	try:
		if g5 < 4:
			x = x/5
			l5 = l5+6
			paths.append(1)
		else:
			l5 = l5-l5
			g5 = 6/4
			paths.append(2)
		if g5 >= 4:
			x = x/7
			paths.append(3)
		else:
			x = 4+x
			x = l5/6
			x = 1-3
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