import numpy as np 

def function(x):

	b9 = 2
	d9 = 5
	paths = []
	try:
		if b9 > 4:
			x = d9*3
			paths.append(1)
		else:
			b9 = 6-b9
			b9 = 9*d9
			paths.append(2)
		if b9 < 2:
			x = d9+7
			d9 = 0*1
			b9 = d9+3
			paths.append(3)
		else:
			d9 = 9+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))