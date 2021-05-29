import numpy as np 

def function(x):

	j7 = 9
	g1 = x
	paths = []
	try:
		if j7 > 1:
			g1 = g1-g1
			g1 = g1/j7
			g1 = g1+j7
			paths.append(1)
		else:
			x = 1/j7
			paths.append(2)
		if g1 >= 5:
			g1 = 9/g1
			g1 = 3/4
			paths.append(3)
		else:
			j7 = j7+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))