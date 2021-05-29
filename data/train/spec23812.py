import numpy as np 

def function(x):

	g5 = 7
	o9 = 1
	paths = []
	try:
		if x > 0:
			o9 = o9/x
			x = x+x
			o9 = 3*g5
			paths.append(1)
		else:
			x = 9*8
			x = x/1
			paths.append(2)
		if o9 > 2:
			g5 = g5*5
			o9 = 4*6
			paths.append(3)
		else:
			g5 = g5*o9
			o9 = o9-g5
			paths.append(4)
		paths.append(5)
		assert o9 >= 0
		g5 = o9**0.5
		return g5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))