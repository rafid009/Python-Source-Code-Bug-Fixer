import numpy as np 

def function(x):

	j1 = x
	g6 = x
	paths = []
	try:
		if g6 < 9:
			g6 = 2+j1
			j1 = 1*x
			j1 = x/9
			paths.append(1)
		else:
			g6 = g6*g6
			j1 = 6/9
			x = x+x
			paths.append(2)
		if g6 > 2:
			g6 = 5-g6
			paths.append(3)
		else:
			x = x-j1
			j1 = j1+j1
			x = 0-1
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		x = j1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))