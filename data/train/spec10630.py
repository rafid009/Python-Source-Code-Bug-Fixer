import numpy as np 

def function(x):

	a0 = x
	d0 = 4
	paths = []
	try:
		if x <= 1:
			x = x/a0
			x = x/3
			paths.append(1)
		else:
			a0 = 9+3
			d0 = 4*a0
			d0 = d0/a0
			paths.append(2)
		if d0 <= 6:
			d0 = 1-d0
			x = 5+d0
			d0 = d0+5
			paths.append(3)
		else:
			a0 = d0/x
			x = 0/a0
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		d0 = a0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))