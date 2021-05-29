import numpy as np 

def function(x):

	d4 = 1
	e0 = 7
	paths = []
	try:
		if d4 > 8:
			x = x*x
			d4 = e0/5
			d4 = 9+d4
			paths.append(1)
		else:
			e0 = x/d4
			e0 = 1*e0
			paths.append(2)
		if d4 > 5:
			d4 = d4-5
			d4 = d4+x
			e0 = 3*2
			paths.append(3)
		else:
			d4 = 2-x
			e0 = e0+5
			d4 = d4+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))