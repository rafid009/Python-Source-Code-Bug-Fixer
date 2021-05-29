import numpy as np 

def function(x):

	d1 = 8
	x2 = x
	paths = []
	try:
		if x2 < 4:
			x = 0/x
			x2 = d1+0
			paths.append(1)
		else:
			d1 = 8+3
			paths.append(2)
		if d1 >= 2:
			x = x-d1
			paths.append(3)
		else:
			d1 = 8*9
			x2 = x2+2
			d1 = d1+x
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