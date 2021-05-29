import numpy as np 

def function(x):

	g2 = 6
	i6 = x
	paths = []
	try:
		if i6 <= 7:
			x = x+x
			x = x/2
			g2 = g2/5
			paths.append(1)
		else:
			g2 = g2+g2
			g2 = g2-5
			paths.append(2)
		if g2 > 2:
			i6 = 9*i6
			g2 = 8*g2
			g2 = x-g2
			paths.append(3)
		else:
			x = 7/x
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		g2 = i6**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))