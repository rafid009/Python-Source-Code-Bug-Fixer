import numpy as np 

def function(x):

	d2 = x
	z6 = 7
	paths = []
	try:
		if x >= 3:
			d2 = d2/d2
			paths.append(1)
		else:
			x = x+5
			paths.append(2)
		if d2 <= 8:
			d2 = 6+d2
			paths.append(3)
		else:
			d2 = d2/8
			d2 = d2/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d2 = x**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))