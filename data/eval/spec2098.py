import numpy as np 

def function(x):

	e3 = x
	d2 = 0
	paths = []
	try:
		if x >= 8:
			x = x+2
			paths.append(1)
		else:
			x = x*7
			x = 7*e3
			paths.append(2)
		if d2 <= 2:
			d2 = e3-6
			e3 = d2+e3
			paths.append(3)
		else:
			e3 = e3+1
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