import numpy as np 

def function(x):

	g2 = x
	i8 = 8
	paths = []
	try:
		if x < 3:
			i8 = 0+x
			paths.append(1)
		else:
			x = 7+x
			paths.append(2)
		if i8 >= 9:
			g2 = g2*g2
			g2 = g2/g2
			i8 = 9/9
			paths.append(3)
		else:
			g2 = g2/7
			i8 = 7+i8
			i8 = i8/4
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