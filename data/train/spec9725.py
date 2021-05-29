import numpy as np 

def function(x):

	g9 = 0
	k9 = x
	paths = []
	try:
		if k9 < 2:
			k9 = k9-g9
			x = 1-x
			g9 = g9+9
			paths.append(1)
		else:
			k9 = 5*3
			g9 = g9*9
			paths.append(2)
		if g9 <= 7:
			x = 7-x
			paths.append(3)
		else:
			x = k9+7
			g9 = k9/3
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