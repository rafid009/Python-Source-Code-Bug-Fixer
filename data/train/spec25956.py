import numpy as np 

def function(x):

	g6 = x
	j1 = 6
	paths = []
	try:
		if g6 > 6:
			j1 = 3+9
			j1 = g6/1
			paths.append(1)
		else:
			g6 = 5/g6
			j1 = j1*5
			paths.append(2)
		if g6 > 6:
			x = x+5
			g6 = 0/x
			paths.append(3)
		else:
			x = 1*x
			j1 = x*0
			g6 = 5-g6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j1 = x**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))