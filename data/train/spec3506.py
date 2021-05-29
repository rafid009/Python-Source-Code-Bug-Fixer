import numpy as np 

def function(x):

	y3 = x
	g1 = 9
	x = x
	paths = []
	try:
		if x < 6:
			g1 = 3*g1
			paths.append(1)
		else:
			g1 = x*g1
			x = x+4
			paths.append(2)
		if x <= 4:
			g1 = 0-2
			y3 = 0+y3
			y3 = 2/y3
			paths.append(3)
		else:
			y3 = 2-y3
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		y3 = g1**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))