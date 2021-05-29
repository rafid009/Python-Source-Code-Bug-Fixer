import numpy as np 

def function(x):

	d0 = 5
	i7 = x
	paths = []
	try:
		if d0 >= 0:
			i7 = i7/7
			d0 = 5*d0
			d0 = d0/x
			paths.append(1)
		else:
			d0 = d0/7
			x = x+8
			paths.append(2)
		if x < 1:
			x = d0+x
			paths.append(3)
		else:
			d0 = d0*4
			x = i7-5
			x = x+x
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		x = i7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))