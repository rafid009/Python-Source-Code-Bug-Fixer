import numpy as np 

def function(x):

	d9 = 7
	a0 = 9
	paths = []
	try:
		if x >= 4:
			x = x/1
			a0 = a0/1
			paths.append(1)
		else:
			d9 = a0+0
			a0 = d9+a0
			paths.append(2)
		if a0 >= 7:
			d9 = 7*d9
			d9 = 6-d9
			paths.append(3)
		else:
			x = 6/x
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