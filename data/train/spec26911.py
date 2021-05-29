import numpy as np 

def function(x):

	d6 = 4
	v2 = x
	x = x
	paths = []
	try:
		if v2 <= 0:
			v2 = x*v2
			paths.append(1)
		else:
			v2 = d6+v2
			x = x-d6
			paths.append(2)
		if v2 < 9:
			x = 3*x
			x = 3*7
			v2 = 8+x
			paths.append(3)
		else:
			x = 2/x
			d6 = d6-6
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