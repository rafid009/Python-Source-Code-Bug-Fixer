import numpy as np 

def function(x):

	g4 = 2
	j2 = 8
	paths = []
	try:
		if j2 > 8:
			x = x+4
			g4 = 9-5
			paths.append(1)
		else:
			g4 = 9*j2
			j2 = 8+x
			x = j2/x
			paths.append(2)
		if j2 >= 2:
			g4 = g4-3
			x = x/8
			x = g4/x
			paths.append(3)
		else:
			g4 = g4/x
			g4 = 7-7
			x = x/1
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