import numpy as np 

def function(x):

	d9 = x
	b7 = x
	paths = []
	try:
		if x > 1:
			d9 = d9*b7
			d9 = 0/b7
			paths.append(1)
		else:
			b7 = 1*b7
			d9 = d9*d9
			b7 = 8+b7
			paths.append(2)
		if b7 < 2:
			d9 = d9*d9
			paths.append(3)
		else:
			d9 = x+4
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		d9 = b7**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))