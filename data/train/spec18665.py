import numpy as np 

def function(x):

	y2 = x
	g4 = 0
	paths = []
	try:
		if x > 4:
			y2 = 2+y2
			paths.append(1)
		else:
			g4 = x*3
			paths.append(2)
		if g4 < 9:
			x = 6-x
			x = 3-6
			paths.append(3)
		else:
			y2 = 6+y2
			g4 = g4-g4
			x = 8+x
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		y2 = y2**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))