import numpy as np 

def function(x):

	d6 = 5
	d2 = x
	paths = []
	try:
		if x < 4:
			d2 = x-x
			paths.append(1)
		else:
			d6 = 1-8
			d2 = 3+d6
			paths.append(2)
		if d6 < 8:
			d6 = d6+0
			paths.append(3)
		else:
			x = x/9
			x = 2*d6
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		d6 = d2**0.5
		return d6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))