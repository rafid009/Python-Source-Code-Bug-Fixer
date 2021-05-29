import numpy as np 

def function(x):

	j8 = 4
	g2 = 4
	paths = []
	try:
		if x >= 1:
			g2 = 5/g2
			paths.append(1)
		else:
			j8 = j8+7
			g2 = 2-0
			j8 = 8-j8
			paths.append(2)
		if j8 >= 8:
			x = x+x
			g2 = g2+j8
			x = j8+x
			paths.append(3)
		else:
			j8 = g2*j8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g2 = x**0.5
		return g2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))