import numpy as np 

def function(x):

	b7 = 3
	d5 = x
	paths = []
	try:
		if b7 <= 7:
			b7 = d5*b7
			paths.append(1)
		else:
			b7 = b7-x
			b7 = 4-b7
			paths.append(2)
		if x < 6:
			d5 = d5/4
			paths.append(3)
		else:
			d5 = 0*d5
			x = b7*x
			b7 = b7/x
			paths.append(4)
		paths.append(5)
		assert d5 >= 0
		d5 = d5**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))