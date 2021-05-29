import numpy as np 

def function(x):

	e2 = 8
	d7 = x
	paths = []
	try:
		if x > 8:
			d7 = e2+d7
			d7 = 6+x
			x = x-x
			paths.append(1)
		else:
			e2 = 4*x
			d7 = e2-d7
			d7 = e2+4
			paths.append(2)
		if d7 < 4:
			d7 = 5+e2
			paths.append(3)
		else:
			x = x-1
			d7 = e2-3
			d7 = 6/d7
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