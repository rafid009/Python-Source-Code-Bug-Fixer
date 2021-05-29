import numpy as np 

def function(x):

	g4 = x
	v1 = x
	x = x
	paths = []
	try:
		if x <= 6:
			v1 = 7-v1
			v1 = v1+x
			x = v1-5
			paths.append(1)
		else:
			x = v1+4
			paths.append(2)
		if x <= 6:
			g4 = x-g4
			v1 = v1*g4
			x = v1/2
			paths.append(3)
		else:
			g4 = g4+5
			paths.append(4)
		paths.append(5)
		assert v1 >= 0
		g4 = v1**0.5
		return g4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))