import numpy as np 

def function(x):

	j4 = x
	d8 = 9
	paths = []
	try:
		if d8 <= 0:
			d8 = x*d8
			d8 = 0/8
			paths.append(1)
		else:
			j4 = 0*d8
			paths.append(2)
		if d8 > 8:
			d8 = d8*d8
			j4 = x+1
			d8 = d8-6
			paths.append(3)
		else:
			x = 3+3
			x = d8-x
			d8 = 1*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))