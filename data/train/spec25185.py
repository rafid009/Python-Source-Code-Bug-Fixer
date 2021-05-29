import numpy as np 

def function(x):

	d4 = 9
	r2 = x
	paths = []
	try:
		if x >= 7:
			x = r2/x
			x = r2+x
			paths.append(1)
		else:
			d4 = x*d4
			x = x+4
			x = x-d4
			paths.append(2)
		if x <= 3:
			d4 = d4+8
			paths.append(3)
		else:
			x = x+d4
			r2 = r2/3
			r2 = 5-d4
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