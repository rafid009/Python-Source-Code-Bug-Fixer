import numpy as np 

def function(x):

	j1 = 7
	g2 = x
	paths = []
	try:
		if g2 >= 3:
			g2 = 7*g2
			paths.append(1)
		else:
			j1 = x+j1
			paths.append(2)
		if g2 >= 7:
			x = 5*x
			paths.append(3)
		else:
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert j1 >= 0
		g2 = j1**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))