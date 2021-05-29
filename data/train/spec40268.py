import numpy as np 

def function(x):

	g2 = x
	j5 = 7
	x = 8
	paths = []
	try:
		if x < 5:
			x = x/x
			paths.append(1)
		else:
			g2 = 2-g2
			j5 = j5-9
			x = 9+x
			paths.append(2)
		if x < 2:
			x = j5-9
			j5 = 3/j5
			x = 7-x
			paths.append(3)
		else:
			j5 = 7*j5
			g2 = g2-5
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		g2 = j5**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))