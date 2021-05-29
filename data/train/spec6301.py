import numpy as np 

def function(x):

	y2 = x
	g2 = 4
	paths = []
	try:
		if g2 < 8:
			g2 = 4*0
			paths.append(1)
		else:
			y2 = y2*g2
			paths.append(2)
		if x < 7:
			g2 = x*3
			x = 0*g2
			y2 = g2+9
			paths.append(3)
		else:
			x = 8+x
			x = 6/7
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		g2 = y2**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))