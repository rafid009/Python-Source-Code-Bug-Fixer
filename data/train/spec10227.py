import numpy as np 

def function(x):

	n8 = x
	g2 = 4
	paths = []
	try:
		if g2 >= 5:
			x = 9/x
			x = 7+n8
			n8 = 4+n8
			paths.append(1)
		else:
			x = x/8
			n8 = 2/n8
			paths.append(2)
		if n8 >= 8:
			n8 = n8+5
			g2 = g2*8
			paths.append(3)
		else:
			x = 5+x
			n8 = n8-7
			g2 = g2-n8
			paths.append(4)
		paths.append(5)
		assert n8 >= 0
		g2 = n8**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))