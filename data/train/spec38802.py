import numpy as np 

def function(x):

	d1 = x
	b2 = 5
	paths = []
	try:
		if x <= 2:
			x = 3/x
			d1 = d1-b2
			paths.append(1)
		else:
			b2 = 7+b2
			paths.append(2)
		if x > 8:
			d1 = d1*d1
			paths.append(3)
		else:
			x = d1+d1
			d1 = x/1
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