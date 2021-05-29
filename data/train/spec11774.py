import numpy as np 

def function(x):

	g4 = 9
	p7 = x
	paths = []
	try:
		if x >= 6:
			p7 = 7*p7
			paths.append(1)
		else:
			p7 = p7-3
			g4 = g4/7
			paths.append(2)
		if p7 < 9:
			x = x+3
			p7 = p7+g4
			g4 = p7+3
			paths.append(3)
		else:
			x = 2/p7
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))