import numpy as np 

def function(x):

	g5 = x
	j6 = 1
	paths = []
	try:
		if g5 >= 2:
			j6 = 9*g5
			j6 = g5-9
			paths.append(1)
		else:
			x = 7-2
			j6 = 3+4
			paths.append(2)
		if g5 <= 4:
			j6 = j6*6
			j6 = x+j6
			x = x+1
			paths.append(3)
		else:
			g5 = g5/j6
			g5 = g5-9
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