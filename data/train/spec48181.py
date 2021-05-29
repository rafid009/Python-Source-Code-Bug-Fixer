import numpy as np 

def function(x):

	d0 = 7
	v7 = x
	paths = []
	try:
		if d0 >= 7:
			d0 = 3*v7
			d0 = d0+v7
			x = x+v7
			paths.append(1)
		else:
			d0 = d0/d0
			paths.append(2)
		if v7 >= 6:
			v7 = v7*3
			v7 = v7/4
			v7 = 0+d0
			paths.append(3)
		else:
			v7 = v7+v7
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