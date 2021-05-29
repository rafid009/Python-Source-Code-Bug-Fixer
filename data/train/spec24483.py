import numpy as np 

def function(x):

	b1 = 7
	d5 = 6
	paths = []
	try:
		if x <= 3:
			x = 4*x
			b1 = 6+x
			paths.append(1)
		else:
			d5 = 6*d5
			paths.append(2)
		if x < 6:
			b1 = b1-6
			x = 1-8
			b1 = b1/b1
			paths.append(3)
		else:
			d5 = 3/d5
			b1 = b1+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))