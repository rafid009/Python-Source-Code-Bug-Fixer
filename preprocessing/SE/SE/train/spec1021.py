import numpy as np 

def function(x):

	o8 = x
	g2 = 2
	paths = []
	try:
		if g2 > 8:
			x = x/7
			paths.append(1)
		else:
			x = g2/2
			g2 = x/9
			g2 = g2+0
			paths.append(2)
		if x < 3:
			x = 5+x
			paths.append(3)
		else:
			o8 = o8*9
			o8 = o8+o8
			paths.append(4)
		paths.append(5)
		assert o8 >= 0
		g2 = o8**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))