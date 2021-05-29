import numpy as np 

def function(x):

	n4 = x
	g9 = x
	paths = []
	try:
		if n4 < 6:
			n4 = n4-3
			paths.append(1)
		else:
			x = 8/1
			g9 = g9+2
			n4 = n4/9
			paths.append(2)
		if g9 < 0:
			g9 = 1+g9
			g9 = n4*8
			g9 = g9+1
			paths.append(3)
		else:
			n4 = 3/x
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		x = g9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))