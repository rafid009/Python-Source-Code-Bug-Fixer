import numpy as np 

def function(x):

	b6 = x
	g4 = 9
	paths = []
	try:
		if x >= 5:
			b6 = 2-b6
			x = x+8
			paths.append(1)
		else:
			b6 = 9+b6
			b6 = b6+3
			b6 = b6+6
			paths.append(2)
		if g4 < 0:
			x = x/b6
			b6 = b6-b6
			paths.append(3)
		else:
			x = x+5
			b6 = 2/b6
			x = 2+0
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		g4 = b6**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))