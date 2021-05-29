import numpy as np 

def function(x):

	c2 = x
	d1 = 0
	paths = []
	try:
		if c2 > 2:
			d1 = 9+d1
			x = 3*x
			x = c2*x
			paths.append(1)
		else:
			d1 = d1-c2
			paths.append(2)
		if c2 > 1:
			x = 1+x
			d1 = x+6
			x = 7+x
			paths.append(3)
		else:
			x = x/d1
			paths.append(4)
		paths.append(5)
		assert c2 >= 0
		d1 = c2**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))