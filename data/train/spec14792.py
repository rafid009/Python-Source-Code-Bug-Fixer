import numpy as np 

def function(x):

	j1 = x
	g9 = 3
	x = 3
	paths = []
	try:
		if x <= 3:
			x = x*7
			paths.append(1)
		else:
			j1 = 9/x
			j1 = j1-0
			j1 = g9-3
			paths.append(2)
		if x <= 3:
			g9 = j1+j1
			g9 = 7-g9
			j1 = j1/g9
			paths.append(3)
		else:
			x = 6-x
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		g9 = j1**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))