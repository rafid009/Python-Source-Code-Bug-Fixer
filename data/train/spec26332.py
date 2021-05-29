import numpy as np 

def function(x):

	b1 = 0
	d5 = 5
	paths = []
	try:
		if x >= 6:
			x = x-6
			paths.append(1)
		else:
			d5 = d5-5
			paths.append(2)
		if x <= 0:
			d5 = d5+6
			paths.append(3)
		else:
			x = x/9
			b1 = 1+7
			d5 = d5+2
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