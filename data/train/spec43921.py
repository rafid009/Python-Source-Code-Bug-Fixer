import numpy as np 

def function(x):

	j4 = 4
	g7 = 9
	paths = []
	try:
		if x > 1:
			g7 = j4/g7
			paths.append(1)
		else:
			g7 = j4+3
			j4 = 0*4
			g7 = g7*6
			paths.append(2)
		if g7 > 4:
			j4 = 6/7
			paths.append(3)
		else:
			j4 = j4+0
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j4 = x**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))