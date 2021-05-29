import numpy as np 

def function(x):

	f3 = x
	g4 = x
	paths = []
	try:
		if x > 3:
			g4 = 3-f3
			x = 8-g4
			paths.append(1)
		else:
			x = f3+x
			f3 = f3+f3
			paths.append(2)
		if g4 <= 0:
			x = x*2
			paths.append(3)
		else:
			x = 8+6
			f3 = f3-9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g4 = x**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))