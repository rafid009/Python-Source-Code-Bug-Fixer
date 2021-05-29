import numpy as np 

def function(x):

	g2 = 5
	v7 = 3
	paths = []
	try:
		if v7 >= 7:
			v7 = v7+v7
			g2 = v7/5
			v7 = g2*x
			paths.append(1)
		else:
			v7 = 1+v7
			g2 = 9-g2
			paths.append(2)
		if g2 > 8:
			v7 = x-v7
			v7 = 0-v7
			paths.append(3)
		else:
			g2 = x+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v7 = x**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))