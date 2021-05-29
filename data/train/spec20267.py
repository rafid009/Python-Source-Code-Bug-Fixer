import numpy as np 

def function(x):

	d5 = x
	g3 = x
	paths = []
	try:
		if g3 >= 9:
			g3 = d5/d5
			d5 = 1*x
			paths.append(1)
		else:
			g3 = g3*7
			paths.append(2)
		if g3 <= 2:
			d5 = x-0
			d5 = d5-8
			paths.append(3)
		else:
			x = 7+5
			x = d5/8
			paths.append(4)
		paths.append(5)
		assert g3 >= 0
		x = g3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))