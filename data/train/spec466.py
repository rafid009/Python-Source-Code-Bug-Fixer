import numpy as np 

def function(x):

	q0 = x
	r2 = 5
	paths = []
	try:
		if q0 >= 0:
			r2 = r2/3
			x = x*q0
			q0 = x*x
			paths.append(1)
		else:
			r2 = q0-r2
			paths.append(2)
		if x <= 6:
			x = 5*x
			r2 = 8+x
			r2 = q0-r2
			paths.append(3)
		else:
			x = x/1
			r2 = r2-8
			x = 7*4
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