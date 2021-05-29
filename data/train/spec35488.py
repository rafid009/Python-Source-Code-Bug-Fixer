import numpy as np 

def function(x):

	g9 = x
	y2 = x
	paths = []
	try:
		if x >= 7:
			y2 = y2-x
			x = 5*5
			y2 = 5+y2
			paths.append(1)
		else:
			x = x*y2
			x = x/1
			paths.append(2)
		if x <= 9:
			x = x/2
			y2 = x-y2
			paths.append(3)
		else:
			g9 = 4+g9
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		g9 = y2**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))