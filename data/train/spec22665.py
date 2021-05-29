import numpy as np 

def function(x):

	d8 = x
	g9 = 4
	x = 4
	paths = []
	try:
		if d8 > 8:
			x = d8-9
			x = x+0
			g9 = g9-4
			paths.append(1)
		else:
			g9 = g9/x
			d8 = 3/d8
			d8 = 9*3
			paths.append(2)
		if x < 7:
			x = x+8
			x = x/6
			paths.append(3)
		else:
			g9 = 8/8
			g9 = g9-3
			x = d8*1
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