import numpy as np 

def function(x):

	b3 = 7
	d5 = 6
	paths = []
	try:
		if x < 7:
			d5 = x*d5
			x = x/d5
			paths.append(1)
		else:
			b3 = b3*5
			d5 = d5-6
			paths.append(2)
		if d5 >= 1:
			d5 = d5/x
			paths.append(3)
		else:
			d5 = 9/3
			x = 0-x
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