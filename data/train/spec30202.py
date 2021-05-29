import numpy as np 

def function(x):

	g1 = x
	y5 = 6
	x = x
	paths = []
	try:
		if g1 >= 2:
			y5 = 8*0
			g1 = g1+6
			g1 = g1/8
			paths.append(1)
		else:
			x = x+4
			x = 2+3
			y5 = y5/6
			paths.append(2)
		if y5 > 4:
			g1 = g1/6
			paths.append(3)
		else:
			x = 7-x
			y5 = y5-7
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		x = g1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))