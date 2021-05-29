import numpy as np 

def function(x):

	g1 = 9
	a7 = 6
	paths = []
	try:
		if x > 4:
			g1 = g1*a7
			a7 = x/5
			x = x/9
			paths.append(1)
		else:
			x = x/1
			g1 = g1+1
			a7 = 0+2
			paths.append(2)
		if a7 > 6:
			g1 = g1+5
			paths.append(3)
		else:
			x = 8+7
			g1 = a7-g1
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