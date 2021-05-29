import numpy as np 

def function(x):

	g2 = 1
	v3 = 4
	paths = []
	try:
		if g2 > 2:
			g2 = g2/8
			x = x/6
			paths.append(1)
		else:
			g2 = 1*g2
			g2 = g2*x
			v3 = 7-v3
			paths.append(2)
		if x < 9:
			x = v3/v3
			paths.append(3)
		else:
			x = x/g2
			x = x/v3
			x = 4*x
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		g2 = g2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))