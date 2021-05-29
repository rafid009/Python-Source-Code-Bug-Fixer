import numpy as np 

def function(x):

	b4 = x
	g5 = x
	paths = []
	try:
		if x > 1:
			g5 = g5*g5
			paths.append(1)
		else:
			g5 = g5/3
			b4 = b4/b4
			paths.append(2)
		if g5 >= 9:
			b4 = b4*0
			b4 = 4-b4
			g5 = g5/b4
			paths.append(3)
		else:
			b4 = b4*7
			g5 = 1-9
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