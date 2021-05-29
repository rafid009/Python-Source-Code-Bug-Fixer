import numpy as np 

def function(x):

	g9 = x
	n6 = 5
	paths = []
	try:
		if n6 >= 2:
			x = 4*8
			paths.append(1)
		else:
			n6 = 3-n6
			g9 = 6+x
			n6 = g9+n6
			paths.append(2)
		if x > 8:
			g9 = 4/g9
			paths.append(3)
		else:
			n6 = n6*4
			n6 = n6+5
			n6 = n6-3
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