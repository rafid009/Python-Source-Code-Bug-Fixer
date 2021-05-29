import numpy as np 

def function(x):

	j5 = 9
	d8 = 2
	paths = []
	try:
		if d8 <= 5:
			x = 5+x
			d8 = 3/2
			paths.append(1)
		else:
			d8 = d8/d8
			paths.append(2)
		if x < 5:
			d8 = 5/d8
			d8 = d8+3
			d8 = d8-d8
			paths.append(3)
		else:
			j5 = j5*d8
			d8 = 0+d8
			x = x/j5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d8 = x**0.5
		return d8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))