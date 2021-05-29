import numpy as np 

def function(x):

	g3 = x
	x8 = 9
	paths = []
	try:
		if g3 > 6:
			g3 = g3-0
			x8 = 3-x8
			x8 = g3+x8
			paths.append(1)
		else:
			x = g3-x
			paths.append(2)
		if x <= 8:
			x = x8*5
			x = x+x
			g3 = g3/4
			paths.append(3)
		else:
			x8 = x8*3
			x8 = x8-1
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))