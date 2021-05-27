import numpy as np 

def function(x):

	d9 = x
	b2 = 4
	paths = []
	try:
		if x > 6:
			b2 = 5+6
			d9 = x+2
			b2 = b2*6
			paths.append(1)
		else:
			b2 = 1-x
			paths.append(2)
		if x <= 9:
			d9 = d9*4
			paths.append(3)
		else:
			d9 = 4-4
			x = 0*2
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		d9 = b2**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))