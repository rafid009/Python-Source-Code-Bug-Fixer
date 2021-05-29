import numpy as np 

def function(x):

	i5 = x
	d0 = x
	paths = []
	try:
		if x <= 0:
			x = 0*x
			x = x-2
			paths.append(1)
		else:
			i5 = i5*2
			d0 = d0-7
			paths.append(2)
		if d0 > 2:
			i5 = d0/3
			x = x*4
			paths.append(3)
		else:
			d0 = d0/x
			d0 = 4*d0
			i5 = 8+d0
			paths.append(4)
		paths.append(5)
		assert i5 >= 0
		d0 = i5**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))