import numpy as np 

def function(x):

	d2 = x
	n0 = x
	paths = []
	try:
		if x <= 9:
			x = 2-x
			paths.append(1)
		else:
			x = x*7
			d2 = 7*x
			paths.append(2)
		if n0 >= 3:
			x = 4/x
			x = 8*5
			paths.append(3)
		else:
			x = x/d2
			d2 = d2+3
			paths.append(4)
		paths.append(5)
		assert n0 >= 0
		d2 = n0**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))