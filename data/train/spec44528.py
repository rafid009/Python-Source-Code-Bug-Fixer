import numpy as np 

def function(x):

	n0 = x
	d0 = 6
	paths = []
	try:
		if x < 7:
			d0 = 3-d0
			paths.append(1)
		else:
			n0 = 8+x
			x = 7+1
			paths.append(2)
		if d0 >= 3:
			x = x*6
			d0 = 7*d0
			d0 = x+0
			paths.append(3)
		else:
			x = x+x
			d0 = d0*4
			d0 = n0+d0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d0 = x**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))