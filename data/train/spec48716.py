import numpy as np 

def function(x):

	d4 = x
	g8 = x
	paths = []
	try:
		if g8 >= 1:
			g8 = 7*g8
			paths.append(1)
		else:
			g8 = 9/g8
			paths.append(2)
		if x <= 1:
			g8 = g8/6
			d4 = 0/d4
			paths.append(3)
		else:
			g8 = 7*d4
			g8 = d4/x
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		d4 = g8**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))