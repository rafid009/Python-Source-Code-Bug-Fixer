import numpy as np 

def function(x):

	l6 = 9
	g5 = x
	paths = []
	try:
		if x <= 4:
			x = x/4
			x = g5*x
			l6 = 1-l6
			paths.append(1)
		else:
			x = 3*4
			paths.append(2)
		if g5 <= 4:
			l6 = 0-l6
			paths.append(3)
		else:
			g5 = g5*l6
			l6 = 3+l6
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))