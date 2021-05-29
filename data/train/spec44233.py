import numpy as np 

def function(x):

	a9 = x
	g7 = x
	paths = []
	try:
		if x > 4:
			x = x+5
			g7 = g7-8
			paths.append(1)
		else:
			a9 = a9+x
			paths.append(2)
		if a9 > 1:
			a9 = x-9
			paths.append(3)
		else:
			x = x*g7
			a9 = g7-x
			a9 = 7*a9
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		x = a9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))