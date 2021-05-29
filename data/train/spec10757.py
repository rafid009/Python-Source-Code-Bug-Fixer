import numpy as np 

def function(x):

	d8 = 6
	d5 = x
	paths = []
	try:
		if d8 >= 0:
			x = x/3
			d8 = d8+9
			paths.append(1)
		else:
			d5 = 3-d5
			d8 = 0-d8
			paths.append(2)
		if x < 3:
			d8 = d8+5
			paths.append(3)
		else:
			d5 = d8/7
			x = x*9
			x = 0+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d5 = x**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))