import numpy as np 

def function(x):

	g9 = 9
	f1 = 5
	x = 1
	paths = []
	try:
		if x >= 2:
			x = x+x
			x = x-3
			paths.append(1)
		else:
			g9 = 5*g9
			paths.append(2)
		if g9 < 9:
			x = x-8
			f1 = 1/x
			x = g9+x
			paths.append(3)
		else:
			x = 9*x
			f1 = f1/4
			g9 = 5-8
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))