import numpy as np 

def function(x):

	l5 = x
	g5 = 9
	paths = []
	try:
		if l5 < 3:
			g5 = g5*2
			g5 = g5*3
			x = 3*9
			paths.append(1)
		else:
			g5 = 4*9
			g5 = g5/x
			g5 = 9+g5
			paths.append(2)
		if l5 <= 6:
			g5 = l5/g5
			x = 9+x
			x = 1+l5
			paths.append(3)
		else:
			x = 1/x
			l5 = 4-x
			paths.append(4)
		paths.append(5)
		assert l5 >= 0
		x = l5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))