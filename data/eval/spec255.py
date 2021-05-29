import numpy as np 

def function(x):

	d4 = 7
	q0 = 6
	paths = []
	try:
		if d4 >= 2:
			d4 = 4*d4
			q0 = x/q0
			d4 = 2*9
			paths.append(1)
		else:
			q0 = 5/4
			q0 = 5-9
			d4 = d4*8
			paths.append(2)
		if x >= 1:
			x = 9/5
			x = 4-x
			x = x*x
			paths.append(3)
		else:
			d4 = x+6
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		d4 = q0**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))