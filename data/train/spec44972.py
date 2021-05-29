import numpy as np 

def function(x):

	k2 = x
	g9 = x
	paths = []
	try:
		if x <= 8:
			k2 = g9*k2
			k2 = 6-7
			g9 = k2+g9
			paths.append(1)
		else:
			g9 = g9+8
			paths.append(2)
		if x <= 1:
			x = k2-7
			x = x/x
			paths.append(3)
		else:
			g9 = g9/4
			g9 = 7+g9
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		k2 = g9**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))