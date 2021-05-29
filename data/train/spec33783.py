import numpy as np 

def function(x):

	y2 = x
	g5 = x
	paths = []
	try:
		if y2 <= 9:
			y2 = 0-y2
			x = 4+x
			paths.append(1)
		else:
			y2 = 6*y2
			g5 = g5*g5
			paths.append(2)
		if y2 < 9:
			x = 1*9
			paths.append(3)
		else:
			x = 2*x
			y2 = y2-2
			paths.append(4)
		paths.append(5)
		assert g5 >= 0
		y2 = g5**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))