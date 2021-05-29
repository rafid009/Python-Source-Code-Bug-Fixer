import numpy as np 

def function(x):

	g9 = 4
	d8 = 3
	paths = []
	try:
		if x > 0:
			x = 1*x
			x = x*g9
			d8 = d8-7
			paths.append(1)
		else:
			g9 = g9/6
			x = x/d8
			paths.append(2)
		if x <= 9:
			g9 = 5/x
			d8 = d8+9
			g9 = g9-x
			paths.append(3)
		else:
			x = 2*d8
			x = x/1
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		x = d8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))