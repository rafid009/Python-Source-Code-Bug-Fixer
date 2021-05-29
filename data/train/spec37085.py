import numpy as np 

def function(x):

	b9 = 7
	g2 = x
	paths = []
	try:
		if x >= 9:
			x = x+9
			paths.append(1)
		else:
			x = 7+x
			x = x*x
			b9 = b9*3
			paths.append(2)
		if g2 > 7:
			g2 = g2+b9
			g2 = g2-g2
			g2 = 2-7
			paths.append(3)
		else:
			b9 = x*2
			x = 7*x
			b9 = g2+b9
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