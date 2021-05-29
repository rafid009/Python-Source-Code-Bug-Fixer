import numpy as np 

def function(x):

	g6 = x
	j3 = x
	paths = []
	try:
		if x <= 1:
			g6 = 0/3
			paths.append(1)
		else:
			x = 6-x
			paths.append(2)
		if x < 0:
			x = x/j3
			g6 = j3*8
			g6 = x+4
			paths.append(3)
		else:
			j3 = j3+x
			paths.append(4)
		paths.append(5)
		assert j3 >= 0
		g6 = j3**0.5
		return g6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))