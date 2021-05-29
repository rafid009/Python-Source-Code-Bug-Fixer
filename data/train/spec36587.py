import numpy as np 

def function(x):

	g2 = 7
	v9 = x
	x = 6
	paths = []
	try:
		if v9 > 6:
			v9 = 5-1
			paths.append(1)
		else:
			g2 = 6/v9
			g2 = x-5
			x = 4+x
			paths.append(2)
		if x > 1:
			x = v9+x
			v9 = 2-0
			g2 = g2/9
			paths.append(3)
		else:
			v9 = 9+g2
			g2 = v9/g2
			v9 = g2/6
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