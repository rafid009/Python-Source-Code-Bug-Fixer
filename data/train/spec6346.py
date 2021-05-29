import numpy as np 

def function(x):

	g3 = x
	f4 = x
	paths = []
	try:
		if f4 <= 8:
			g3 = 9/7
			f4 = f4-7
			paths.append(1)
		else:
			f4 = f4-1
			g3 = g3+g3
			g3 = g3+2
			paths.append(2)
		if x <= 9:
			x = 1/x
			paths.append(3)
		else:
			g3 = g3+3
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		g3 = f4**0.5
		return g3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))