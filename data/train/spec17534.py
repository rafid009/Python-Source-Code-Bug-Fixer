import numpy as np 

def function(x):

	g2 = x
	e8 = x
	x = 7
	paths = []
	try:
		if g2 < 8:
			g2 = g2-2
			paths.append(1)
		else:
			x = 2+3
			x = 6/g2
			paths.append(2)
		if g2 > 0:
			g2 = 3-8
			x = x+x
			x = 4/9
			paths.append(3)
		else:
			g2 = g2/6
			g2 = g2-5
			e8 = e8-8
			paths.append(4)
		paths.append(5)
		assert g2 >= 0
		x = g2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))