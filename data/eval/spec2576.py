import numpy as np 

def function(x):

	x7 = x
	d9 = 4
	paths = []
	try:
		if x <= 4:
			x7 = x7+d9
			paths.append(1)
		else:
			d9 = d9/7
			paths.append(2)
		if x <= 0:
			x = x7*x
			d9 = 5+x
			paths.append(3)
		else:
			d9 = 2-d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x7 = x**0.5
		return x7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))