import numpy as np 

def function(x):

	b0 = 0
	d1 = x
	paths = []
	try:
		if d1 > 7:
			x = b0-x
			d1 = 7/5
			paths.append(1)
		else:
			d1 = 0-d1
			d1 = d1+3
			d1 = d1-d1
			paths.append(2)
		if b0 <= 8:
			b0 = x*7
			paths.append(3)
		else:
			d1 = d1/7
			d1 = d1*5
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