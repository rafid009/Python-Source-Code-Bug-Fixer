import numpy as np 

def function(x):

	d5 = 2
	a8 = 4
	paths = []
	try:
		if x < 5:
			a8 = 7*a8
			a8 = 5/a8
			a8 = 9+a8
			paths.append(1)
		else:
			x = x*8
			a8 = 8*2
			d5 = 9*d5
			paths.append(2)
		if a8 < 7:
			x = 8-x
			a8 = 7+3
			paths.append(3)
		else:
			d5 = 7*x
			a8 = a8/a8
			x = x/3
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))