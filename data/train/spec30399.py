import numpy as np 

def function(x):

	d4 = 9
	x9 = x
	paths = []
	try:
		if d4 > 5:
			d4 = x9+0
			x9 = 8*x9
			x = x-2
			paths.append(1)
		else:
			d4 = 8+d4
			paths.append(2)
		if x < 8:
			x = 0/x
			d4 = 9/3
			paths.append(3)
		else:
			x = d4*x
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		d4 = x9**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))