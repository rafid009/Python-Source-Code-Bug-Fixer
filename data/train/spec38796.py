import numpy as np 

def function(x):

	d9 = 1
	g8 = x
	paths = []
	try:
		if d9 >= 8:
			d9 = 9/5
			x = x*2
			x = x+g8
			paths.append(1)
		else:
			g8 = g8*9
			x = g8-1
			paths.append(2)
		if d9 <= 5:
			g8 = g8+0
			d9 = g8/g8
			paths.append(3)
		else:
			d9 = d9+x
			g8 = g8-2
			g8 = 4+g8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))