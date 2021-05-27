import numpy as np 

def function(x):

	d1 = 7
	e4 = x
	paths = []
	try:
		if d1 < 2:
			d1 = 0-d1
			d1 = 5-d1
			d1 = d1+5
			paths.append(1)
		else:
			d1 = x+d1
			e4 = 6+e4
			paths.append(2)
		if e4 < 4:
			d1 = d1*3
			e4 = e4-e4
			d1 = 0+d1
			paths.append(3)
		else:
			e4 = x*4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))