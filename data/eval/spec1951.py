import numpy as np 

def function(x):

	d8 = 3
	d2 = 2
	x = 4
	paths = []
	try:
		if x < 1:
			x = x+0
			paths.append(1)
		else:
			d8 = 0-d8
			x = x-7
			d2 = d2+d2
			paths.append(2)
		if d8 > 7:
			x = x/8
			paths.append(3)
		else:
			d2 = x*9
			d8 = x-1
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