import numpy as np 

def function(x):

	g7 = 3
	j9 = 5
	paths = []
	try:
		if j9 >= 2:
			x = 7*x
			paths.append(1)
		else:
			x = 3*x
			g7 = g7+5
			paths.append(2)
		if j9 <= 0:
			g7 = 1-5
			x = 4/x
			j9 = j9/7
			paths.append(3)
		else:
			g7 = x/1
			paths.append(4)
		paths.append(5)
		assert g7 >= 0
		j9 = g7**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))