import numpy as np 

def function(x):

	v6 = 2
	g1 = 4
	x = 2
	paths = []
	try:
		if v6 > 5:
			x = v6*x
			v6 = 9*v6
			x = x*8
			paths.append(1)
		else:
			g1 = x+v6
			x = v6*g1
			paths.append(2)
		if x < 4:
			x = x*g1
			paths.append(3)
		else:
			g1 = g1-8
			g1 = g1/2
			x = 1+3
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		g1 = g1**0.5
		return g1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))