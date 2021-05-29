import numpy as np 

def function(x):

	n9 = 0
	g9 = x
	x = x
	paths = []
	try:
		if g9 <= 3:
			n9 = 3-x
			paths.append(1)
		else:
			g9 = g9/5
			n9 = x*3
			g9 = 4-g9
			paths.append(2)
		if x >= 5:
			g9 = 0-g9
			g9 = 9/n9
			g9 = 1*g9
			paths.append(3)
		else:
			n9 = 3+g9
			g9 = g9-1
			x = x/8
			paths.append(4)
		paths.append(5)
		assert n9 >= 0
		g9 = n9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))