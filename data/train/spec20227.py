import numpy as np 

def function(x):

	q2 = x
	d8 = 9
	paths = []
	try:
		if d8 > 7:
			d8 = q2/4
			d8 = d8-6
			x = 0+x
			paths.append(1)
		else:
			d8 = d8*d8
			q2 = q2*x
			paths.append(2)
		if x < 8:
			d8 = d8+x
			paths.append(3)
		else:
			d8 = q2*d8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))