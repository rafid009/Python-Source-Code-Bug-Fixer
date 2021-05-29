import numpy as np 

def function(x):

	g2 = 5
	a9 = x
	paths = []
	try:
		if a9 >= 2:
			x = x-a9
			paths.append(1)
		else:
			g2 = 3-g2
			x = x-a9
			paths.append(2)
		if a9 < 3:
			g2 = a9*g2
			x = x-8
			g2 = g2-g2
			paths.append(3)
		else:
			a9 = a9-x
			a9 = 9+x
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))