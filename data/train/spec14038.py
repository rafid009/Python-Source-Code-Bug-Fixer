import numpy as np 

def function(x):

	j8 = x
	g1 = 2
	paths = []
	try:
		if x >= 3:
			x = 2*9
			x = x+5
			paths.append(1)
		else:
			j8 = 3*j8
			g1 = 1*3
			x = 3/x
			paths.append(2)
		if j8 > 1:
			g1 = 4/6
			j8 = j8+9
			g1 = g1/4
			paths.append(3)
		else:
			g1 = g1+9
			j8 = 8-g1
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		g1 = j8**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))