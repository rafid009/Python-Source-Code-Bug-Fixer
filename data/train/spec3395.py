import numpy as np 

def function(x):

	d0 = 3
	e6 = 2
	paths = []
	try:
		if e6 <= 1:
			d0 = d0*d0
			e6 = x*e6
			paths.append(1)
		else:
			e6 = e6*e6
			d0 = x*1
			paths.append(2)
		if x >= 7:
			x = x*5
			x = x-d0
			d0 = x*8
			paths.append(3)
		else:
			d0 = e6*d0
			d0 = d0+1
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		x = d0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))