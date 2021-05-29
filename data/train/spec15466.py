import numpy as np 

def function(x):

	g4 = 3
	j1 = 9
	paths = []
	try:
		if j1 < 0:
			x = x/x
			paths.append(1)
		else:
			x = x-2
			j1 = g4+j1
			g4 = 6-g4
			paths.append(2)
		if j1 >= 5:
			g4 = 6*g4
			x = x-4
			g4 = g4/x
			paths.append(3)
		else:
			j1 = j1*5
			j1 = 0-j1
			j1 = 9+j1
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		j1 = g4**0.5
		return j1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))