import numpy as np 

def function(x):

	d6 = x
	n2 = 9
	x = x
	paths = []
	try:
		if n2 < 9:
			x = x*2
			n2 = n2*x
			paths.append(1)
		else:
			n2 = 0-7
			d6 = d6*4
			paths.append(2)
		if d6 >= 8:
			d6 = n2*2
			n2 = n2+6
			n2 = 8*n2
			paths.append(3)
		else:
			x = x-2
			paths.append(4)
		paths.append(5)
		assert d6 >= 0
		d6 = d6**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))