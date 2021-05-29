import numpy as np 

def function(x):

	d8 = 2
	x9 = x
	paths = []
	try:
		if d8 <= 7:
			x = 9-x
			d8 = 0-d8
			paths.append(1)
		else:
			x = 0/x
			paths.append(2)
		if d8 >= 7:
			x9 = 8+x9
			paths.append(3)
		else:
			x = x*4
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		d8 = x9**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))