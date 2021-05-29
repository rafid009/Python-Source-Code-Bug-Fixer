import numpy as np 

def function(x):

	d8 = x
	v1 = x
	paths = []
	try:
		if d8 <= 6:
			x = x+v1
			d8 = d8+5
			paths.append(1)
		else:
			x = x/d8
			v1 = 2+v1
			paths.append(2)
		if x >= 2:
			d8 = 5*v1
			paths.append(3)
		else:
			x = 1-5
			x = x*8
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