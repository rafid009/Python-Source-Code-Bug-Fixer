import numpy as np 

def function(x):

	g2 = x
	v7 = x
	x = 5
	paths = []
	try:
		if v7 >= 8:
			x = x-x
			paths.append(1)
		else:
			x = v7*x
			paths.append(2)
		if x < 0:
			v7 = v7+2
			paths.append(3)
		else:
			g2 = x*3
			x = v7/6
			g2 = g2+1
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