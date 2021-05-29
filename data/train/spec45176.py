import numpy as np 

def function(x):

	d7 = 9
	g4 = 5
	paths = []
	try:
		if g4 >= 3:
			g4 = g4*5
			g4 = 4-d7
			g4 = x*8
			paths.append(1)
		else:
			x = x-9
			g4 = 0+d7
			g4 = x+g4
			paths.append(2)
		if d7 < 1:
			x = g4*d7
			d7 = 5/d7
			g4 = g4*d7
			paths.append(3)
		else:
			x = x+5
			d7 = 7-1
			d7 = d7/3
			paths.append(4)
		paths.append(5)
		assert g4 >= 0
		d7 = g4**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))