import numpy as np 

def function(x):

	f4 = x
	g8 = 5
	paths = []
	try:
		if f4 <= 8:
			f4 = x-1
			f4 = f4/2
			paths.append(1)
		else:
			f4 = 4+f4
			paths.append(2)
		if x <= 8:
			g8 = g8/9
			f4 = f4+f4
			f4 = 4-f4
			paths.append(3)
		else:
			x = f4*9
			g8 = g8*9
			f4 = 0/f4
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		g8 = f4**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))