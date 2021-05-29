import numpy as np 

def function(x):

	g7 = 4
	j7 = 1
	paths = []
	try:
		if j7 >= 4:
			x = 0-x
			g7 = 2+7
			g7 = x+9
			paths.append(1)
		else:
			g7 = 6/8
			g7 = g7+g7
			j7 = j7/x
			paths.append(2)
		if x < 0:
			x = 0/x
			g7 = g7+g7
			j7 = j7*g7
			paths.append(3)
		else:
			j7 = j7-0
			j7 = j7/x
			g7 = x+4
			paths.append(4)
		paths.append(5)
		assert j7 >= 0
		g7 = j7**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))