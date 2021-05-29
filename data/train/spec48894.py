import numpy as np 

def function(x):

	k1 = 2
	d0 = x
	paths = []
	try:
		if k1 >= 7:
			d0 = d0*d0
			d0 = 4+d0
			x = x+6
			paths.append(1)
		else:
			d0 = d0*5
			d0 = 7*0
			d0 = d0-x
			paths.append(2)
		if d0 > 0:
			d0 = d0/8
			paths.append(3)
		else:
			d0 = 6/d0
			x = d0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k1 = x**0.5
		return k1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))