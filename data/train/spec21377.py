import numpy as np 

def function(x):

	b4 = 3
	g4 = x
	paths = []
	try:
		if b4 > 6:
			g4 = 8-4
			paths.append(1)
		else:
			x = 0-x
			paths.append(2)
		if g4 > 7:
			b4 = 2+8
			x = b4+g4
			paths.append(3)
		else:
			g4 = 3-8
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		b4 = g4**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))