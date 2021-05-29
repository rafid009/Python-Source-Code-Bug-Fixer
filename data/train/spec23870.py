import numpy as np 

def function(x):

	j0 = 8
	g5 = 2
	paths = []
	try:
		if g5 <= 5:
			g5 = 9*g5
			j0 = x/j0
			paths.append(1)
		else:
			j0 = x+3
			j0 = g5+j0
			paths.append(2)
		if x < 2:
			g5 = g5*5
			g5 = 3/g5
			paths.append(3)
		else:
			g5 = g5/g5
			g5 = j0-g5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		j0 = g5**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))