import numpy as np 

def function(x):

	d0 = x
	f1 = 2
	paths = []
	try:
		if d0 <= 7:
			f1 = f1/f1
			f1 = f1+6
			f1 = x-f1
			paths.append(1)
		else:
			d0 = d0-d0
			f1 = 4+0
			paths.append(2)
		if f1 > 0:
			f1 = 5-x
			paths.append(3)
		else:
			d0 = d0+d0
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