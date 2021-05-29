import numpy as np 

def function(x):

	d9 = 9
	r1 = 2
	paths = []
	try:
		if r1 >= 2:
			r1 = 3*r1
			paths.append(1)
		else:
			x = r1/r1
			r1 = 2+x
			r1 = 5/r1
			paths.append(2)
		if x >= 5:
			x = 2/x
			r1 = r1*d9
			x = 2*6
			paths.append(3)
		else:
			d9 = d9*3
			r1 = r1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))