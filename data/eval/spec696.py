import numpy as np 

def function(x):

	d1 = 8
	x = x
	paths = []
	try:
		if x < 2:
			d1 = d1/d1
			x = 0-d1
			paths.append(1)
		else:
			d1 = 8*1
			d1 = d1*5
			x = 5/x
			paths.append(2)
		if d1 <= 9:
			d1 = d1/9
			d1 = 7*x
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d1 = x**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))