import numpy as np 

def function(x):

	d0 = x
	b2 = x
	paths = []
	try:
		if d0 >= 4:
			x = 7*x
			x = x-7
			paths.append(1)
		else:
			d0 = 8-9
			d0 = 2*5
			paths.append(2)
		if x >= 5:
			x = x/b2
			x = b2+x
			paths.append(3)
		else:
			d0 = 6-d0
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