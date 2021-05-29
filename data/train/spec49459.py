import numpy as np 

def function(x):

	a1 = x
	d8 = x
	paths = []
	try:
		if a1 < 9:
			a1 = 2-d8
			d8 = x-8
			paths.append(1)
		else:
			x = 9+x
			d8 = d8-1
			x = x+0
			paths.append(2)
		if a1 < 1:
			d8 = d8*0
			x = x+5
			paths.append(3)
		else:
			d8 = 0-3
			d8 = d8/7
			a1 = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))