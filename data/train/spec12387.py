import numpy as np 

def function(x):

	g4 = x
	n8 = x
	paths = []
	try:
		if x > 1:
			g4 = 4/4
			x = 3-n8
			paths.append(1)
		else:
			x = n8-n8
			paths.append(2)
		if g4 <= 8:
			n8 = g4+5
			x = 2/n8
			paths.append(3)
		else:
			g4 = x*4
			n8 = 4/x
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		x = n8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))