import numpy as np 

def function(x):

	g2 = x
	n8 = x
	paths = []
	try:
		if g2 >= 2:
			g2 = g2-8
			g2 = 3/g2
			x = 6-x
			paths.append(1)
		else:
			x = n8/x
			x = x*9
			n8 = n8-g2
			paths.append(2)
		if n8 > 5:
			x = x/5
			g2 = 8-0
			paths.append(3)
		else:
			x = n8+6
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		n8 = g2**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))