import numpy as np 

def function(x):

	d9 = x
	q3 = 1
	paths = []
	try:
		if x >= 1:
			x = 0-x
			d9 = d9+d9
			q3 = q3/q3
			paths.append(1)
		else:
			q3 = 0-3
			paths.append(2)
		if d9 < 1:
			x = x+2
			q3 = q3*7
			q3 = 4*q3
			paths.append(3)
		else:
			q3 = x*9
			q3 = d9+0
			paths.append(4)
		paths.append(5)
		assert q3 >= 0
		d9 = q3**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))