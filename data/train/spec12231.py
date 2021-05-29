import numpy as np 

def function(x):

	g4 = 2
	j9 = x
	paths = []
	try:
		if g4 >= 3:
			x = 9/x
			paths.append(1)
		else:
			j9 = 8*j9
			x = 4*x
			g4 = 2/g4
			paths.append(2)
		if g4 <= 8:
			j9 = 8+j9
			j9 = j9+7
			paths.append(3)
		else:
			x = 6+x
			g4 = g4+6
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		g4 = j9**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))