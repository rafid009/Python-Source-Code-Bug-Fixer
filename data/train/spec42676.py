import numpy as np 

def function(x):

	g7 = x
	f9 = x
	paths = []
	try:
		if g7 <= 2:
			g7 = g7+7
			paths.append(1)
		else:
			g7 = f9*g7
			paths.append(2)
		if g7 <= 2:
			f9 = 0+f9
			paths.append(3)
		else:
			g7 = g7+2
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		x = f9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))