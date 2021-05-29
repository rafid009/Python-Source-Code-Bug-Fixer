import numpy as np 

def function(x):

	d9 = x
	b2 = 1
	paths = []
	try:
		if d9 <= 6:
			x = x*3
			b2 = b2*b2
			d9 = x-d9
			paths.append(1)
		else:
			d9 = d9+0
			paths.append(2)
		if b2 >= 9:
			b2 = 8/5
			x = 2*x
			paths.append(3)
		else:
			d9 = x/x
			d9 = x/x
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