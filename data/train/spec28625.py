import numpy as np 

def function(x):

	g5 = 6
	f7 = x
	paths = []
	try:
		if g5 <= 5:
			g5 = f7+0
			f7 = 6+x
			x = 9*x
			paths.append(1)
		else:
			g5 = 1+g5
			g5 = g5*5
			x = 2+x
			paths.append(2)
		if g5 > 3:
			g5 = g5+1
			x = x+f7
			paths.append(3)
		else:
			f7 = f7-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g5 = x**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))