import numpy as np 

def function(x):

	g8 = x
	d8 = 6
	x = 2
	paths = []
	try:
		if x <= 4:
			x = x-1
			g8 = 0+g8
			paths.append(1)
		else:
			g8 = g8-0
			d8 = x*5
			x = x*9
			paths.append(2)
		if d8 > 8:
			x = x-0
			paths.append(3)
		else:
			d8 = 6*d8
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		d8 = g8**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))