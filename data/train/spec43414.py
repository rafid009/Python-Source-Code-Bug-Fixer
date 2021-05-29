import numpy as np 

def function(x):

	d8 = 6
	e3 = x
	paths = []
	try:
		if d8 <= 0:
			e3 = x/e3
			x = 9+3
			paths.append(1)
		else:
			e3 = d8-0
			paths.append(2)
		if x < 7:
			d8 = d8*8
			d8 = d8-1
			d8 = x/5
			paths.append(3)
		else:
			d8 = 8*7
			d8 = 7-0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))