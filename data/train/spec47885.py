import numpy as np 

def function(x):

	p9 = x
	g2 = 8
	paths = []
	try:
		if p9 >= 5:
			x = g2-x
			p9 = p9-8
			paths.append(1)
		else:
			g2 = g2/6
			g2 = g2-g2
			paths.append(2)
		if g2 > 3:
			x = 8-x
			paths.append(3)
		else:
			g2 = g2+x
			g2 = g2+p9
			g2 = p9/g2
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		g2 = p9**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))