import numpy as np 

def function(x):

	y4 = x
	g9 = 3
	paths = []
	try:
		if y4 < 0:
			x = x-9
			g9 = 1*g9
			paths.append(1)
		else:
			y4 = y4+4
			x = x+2
			x = 0*x
			paths.append(2)
		if g9 <= 0:
			x = x-9
			paths.append(3)
		else:
			x = 4/2
			x = 9-y4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		y4 = y4**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))