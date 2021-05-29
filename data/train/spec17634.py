import numpy as np 

def function(x):

	g4 = 4
	v6 = 2
	paths = []
	try:
		if v6 > 1:
			v6 = v6/g4
			x = 8-9
			paths.append(1)
		else:
			g4 = 8+g4
			v6 = 1*3
			paths.append(2)
		if x >= 0:
			g4 = g4*4
			g4 = 5-6
			x = 5-x
			paths.append(3)
		else:
			g4 = x+g4
			x = x*9
			v6 = v6-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v6 = x**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))