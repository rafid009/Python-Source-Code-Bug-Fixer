import numpy as np 

def function(x):

	d6 = 0
	n2 = 6
	paths = []
	try:
		if d6 > 4:
			d6 = d6+d6
			d6 = d6+d6
			paths.append(1)
		else:
			d6 = 1*d6
			d6 = d6/3
			paths.append(2)
		if n2 >= 8:
			x = 8*x
			x = x-2
			n2 = 2*n2
			paths.append(3)
		else:
			n2 = 1+n2
			d6 = n2/2
			d6 = d6*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d6 = x**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))