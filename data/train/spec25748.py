import numpy as np 

def function(x):

	g9 = 2
	y9 = x
	paths = []
	try:
		if x < 9:
			x = x+6
			paths.append(1)
		else:
			x = x+0
			x = x*g9
			paths.append(2)
		if y9 <= 4:
			x = g9*x
			paths.append(3)
		else:
			g9 = 5/8
			g9 = g9-4
			paths.append(4)
		paths.append(5)
		assert y9 >= 0
		g9 = y9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))