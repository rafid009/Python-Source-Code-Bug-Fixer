import numpy as np 

def function(x):

	g4 = 2
	v1 = 9
	paths = []
	try:
		if x <= 9:
			g4 = g4*2
			g4 = g4-8
			v1 = v1+g4
			paths.append(1)
		else:
			g4 = g4+9
			g4 = v1*g4
			v1 = x/v1
			paths.append(2)
		if v1 <= 3:
			v1 = 9-8
			paths.append(3)
		else:
			x = 7+x
			v1 = 7/v1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v1 = x**0.5
		return v1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))