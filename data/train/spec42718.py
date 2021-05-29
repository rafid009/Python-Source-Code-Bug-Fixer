import numpy as np 

def function(x):

	d0 = x
	b7 = 2
	paths = []
	try:
		if b7 > 6:
			x = x*x
			d0 = 4+d0
			paths.append(1)
		else:
			b7 = 1*4
			b7 = b7-x
			b7 = d0*d0
			paths.append(2)
		if d0 > 7:
			b7 = b7+x
			paths.append(3)
		else:
			d0 = d0/8
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		b7 = d0**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))