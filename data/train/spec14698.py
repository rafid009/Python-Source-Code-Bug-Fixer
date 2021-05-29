import numpy as np 

def function(x):

	g5 = 6
	b1 = 5
	paths = []
	try:
		if g5 <= 9:
			b1 = b1-8
			g5 = 2-5
			paths.append(1)
		else:
			x = b1+7
			g5 = g5/5
			x = b1-2
			paths.append(2)
		if g5 > 3:
			x = 1+g5
			g5 = g5/g5
			g5 = 9*g5
			paths.append(3)
		else:
			b1 = b1+6
			b1 = b1-x
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