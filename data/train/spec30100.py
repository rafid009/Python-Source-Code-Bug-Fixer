import numpy as np 

def function(x):

	v4 = x
	g9 = x
	paths = []
	try:
		if v4 < 6:
			g9 = g9/g9
			g9 = g9-4
			paths.append(1)
		else:
			v4 = 3*6
			v4 = 8*v4
			v4 = x/7
			paths.append(2)
		if x <= 3:
			v4 = 9-4
			x = x*x
			paths.append(3)
		else:
			g9 = g9*g9
			x = x-6
			g9 = g9/4
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))