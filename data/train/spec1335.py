import numpy as np 

def function(x):

	g1 = x
	v6 = 8
	paths = []
	try:
		if x >= 9:
			x = g1-0
			x = x/2
			v6 = g1*5
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if v6 > 9:
			v6 = 9+2
			g1 = g1+x
			g1 = 6/g1
			paths.append(3)
		else:
			v6 = v6-v6
			g1 = 6/g1
			v6 = v6+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))