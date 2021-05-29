import numpy as np 

def function(x):

	d5 = x
	q0 = 6
	paths = []
	try:
		if q0 > 5:
			q0 = 5*q0
			paths.append(1)
		else:
			q0 = d5*0
			x = 8-x
			q0 = q0/q0
			paths.append(2)
		if x >= 1:
			q0 = q0-d5
			paths.append(3)
		else:
			x = 1+9
			x = q0*x
			d5 = 9*0
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		x = q0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))