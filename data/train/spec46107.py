import numpy as np 

def function(x):

	g2 = 8
	v9 = x
	x = 1
	paths = []
	try:
		if v9 >= 7:
			x = x+x
			v9 = v9*8
			v9 = 3-v9
			paths.append(1)
		else:
			x = x*6
			paths.append(2)
		if x >= 3:
			x = x/6
			x = v9-g2
			v9 = 5-v9
			paths.append(3)
		else:
			g2 = 9*x
			g2 = 8-g2
			x = x-5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))