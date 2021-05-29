import numpy as np 

def function(x):

	d5 = 5
	g5 = 6
	paths = []
	try:
		if d5 <= 8:
			d5 = d5/d5
			x = d5*x
			paths.append(1)
		else:
			x = x+3
			d5 = d5/1
			paths.append(2)
		if x < 6:
			d5 = d5-3
			x = 2/2
			paths.append(3)
		else:
			d5 = 8*3
			x = 4-x
			g5 = 9+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))