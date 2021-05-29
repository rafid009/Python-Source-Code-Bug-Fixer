import numpy as np 

def function(x):

	d9 = 4
	b9 = 5
	paths = []
	try:
		if b9 > 7:
			b9 = b9/b9
			paths.append(1)
		else:
			d9 = 1-d9
			b9 = 9-b9
			paths.append(2)
		if d9 < 2:
			d9 = 0/d9
			x = x-6
			paths.append(3)
		else:
			b9 = x/d9
			b9 = b9+5
			b9 = b9+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))