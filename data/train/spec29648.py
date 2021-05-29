import numpy as np 

def function(x):

	g4 = 8
	v3 = x
	paths = []
	try:
		if x < 1:
			x = x*3
			paths.append(1)
		else:
			g4 = 3/g4
			v3 = x*g4
			paths.append(2)
		if g4 >= 5:
			x = x/6
			g4 = 2*v3
			v3 = 3*2
			paths.append(3)
		else:
			g4 = 4/4
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		x = g4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))