import numpy as np 

def function(x):

	k2 = 2
	g9 = x
	x = x
	paths = []
	try:
		if x <= 0:
			k2 = k2-6
			k2 = 3*0
			k2 = k2+2
			paths.append(1)
		else:
			k2 = 1*k2
			g9 = 0+x
			paths.append(2)
		if k2 >= 2:
			g9 = 9+g9
			g9 = 4-1
			g9 = x+7
			paths.append(3)
		else:
			g9 = g9/k2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g9 = x**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))