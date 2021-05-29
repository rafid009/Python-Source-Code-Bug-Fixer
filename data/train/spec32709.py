import numpy as np 

def function(x):

	g8 = 7
	b0 = 1
	paths = []
	try:
		if g8 <= 4:
			b0 = b0/2
			g8 = g8+3
			x = 3-b0
			paths.append(1)
		else:
			b0 = 0+b0
			g8 = x/g8
			x = b0+x
			paths.append(2)
		if x <= 0:
			x = 6+x
			x = x+4
			x = 0+0
			paths.append(3)
		else:
			b0 = g8/g8
			g8 = g8+9
			x = g8/x
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		g8 = g8**0.5
		return g8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))