import numpy as np 

def function(x):

	g4 = x
	b9 = 6
	paths = []
	try:
		if g4 <= 5:
			b9 = b9+b9
			x = x/x
			g4 = g4+0
			paths.append(1)
		else:
			b9 = 6+g4
			b9 = 1+5
			paths.append(2)
		if x < 3:
			b9 = 2+0
			x = 8+x
			paths.append(3)
		else:
			x = 0-x
			x = 2/1
			x = g4-2
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		g4 = g4**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))