import numpy as np 

def function(x):

	y4 = x
	g5 = x
	paths = []
	try:
		if x <= 6:
			g5 = y4*g5
			g5 = 1/g5
			paths.append(1)
		else:
			g5 = 1-g5
			x = x*2
			y4 = 5*y4
			paths.append(2)
		if x < 9:
			g5 = 2-g5
			y4 = x+y4
			y4 = x*y4
			paths.append(3)
		else:
			g5 = y4-g5
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		x = g5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))