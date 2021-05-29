import numpy as np 

def function(x):

	j6 = 4
	g1 = x
	paths = []
	try:
		if x < 9:
			j6 = g1/j6
			g1 = x/j6
			paths.append(1)
		else:
			g1 = g1+5
			paths.append(2)
		if j6 > 7:
			j6 = 3+j6
			x = g1+j6
			g1 = g1+7
			paths.append(3)
		else:
			j6 = g1+j6
			g1 = g1*7
			x = x+j6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))