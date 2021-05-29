import numpy as np 

def function(x):

	g5 = 7
	i5 = x
	x = 9
	paths = []
	try:
		if g5 < 6:
			g5 = 4*g5
			x = x/5
			paths.append(1)
		else:
			i5 = 8-4
			i5 = 0-i5
			paths.append(2)
		if x >= 2:
			g5 = i5-3
			paths.append(3)
		else:
			i5 = g5+4
			i5 = i5*i5
			g5 = 0-g5
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