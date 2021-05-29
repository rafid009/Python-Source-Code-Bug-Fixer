import numpy as np 

def function(x):

	g9 = 0
	d1 = x
	paths = []
	try:
		if x <= 7:
			d1 = 7*d1
			g9 = g9*7
			g9 = g9+9
			paths.append(1)
		else:
			x = 1+1
			paths.append(2)
		if d1 <= 4:
			x = 3*x
			paths.append(3)
		else:
			x = x-9
			x = x+4
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))