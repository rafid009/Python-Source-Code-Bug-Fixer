import numpy as np 

def function(x):

	d5 = 0
	v5 = 5
	paths = []
	try:
		if x < 5:
			v5 = 3*x
			paths.append(1)
		else:
			x = d5+2
			paths.append(2)
		if v5 <= 5:
			d5 = 5+4
			paths.append(3)
		else:
			v5 = v5-1
			x = 5/v5
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