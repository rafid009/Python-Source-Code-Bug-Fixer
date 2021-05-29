import numpy as np 

def function(x):

	d4 = 3
	b2 = x
	paths = []
	try:
		if d4 <= 2:
			d4 = 0*d4
			paths.append(1)
		else:
			d4 = 8+d4
			d4 = d4/8
			d4 = b2*d4
			paths.append(2)
		if b2 > 9:
			b2 = b2/d4
			d4 = d4*3
			paths.append(3)
		else:
			b2 = b2-6
			paths.append(4)
		paths.append(5)
		assert b2 >= 0
		d4 = b2**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))