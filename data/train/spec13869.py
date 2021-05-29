import numpy as np 

def function(x):

	l5 = 6
	g5 = 5
	paths = []
	try:
		if x < 4:
			l5 = l5+x
			paths.append(1)
		else:
			l5 = 4*l5
			g5 = g5*7
			g5 = 8-9
			paths.append(2)
		if x > 9:
			l5 = g5/7
			l5 = l5*x
			paths.append(3)
		else:
			l5 = l5/l5
			g5 = g5+9
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		g5 = g5**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))