import numpy as np 

def function(x):

	d6 = 3
	e8 = x
	x = x
	paths = []
	try:
		if x <= 7:
			e8 = e8/e8
			d6 = 4-x
			d6 = e8/3
			paths.append(1)
		else:
			x = x+1
			x = e8*x
			d6 = d6*d6
			paths.append(2)
		if x < 8:
			d6 = d6-x
			d6 = d6*7
			paths.append(3)
		else:
			x = 5-3
			d6 = x+e8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))