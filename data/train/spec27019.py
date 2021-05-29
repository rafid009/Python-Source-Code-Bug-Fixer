import numpy as np 

def function(x):

	f3 = x
	q0 = 5
	paths = []
	try:
		if x >= 8:
			f3 = 2+4
			x = 4-x
			q0 = q0-0
			paths.append(1)
		else:
			x = 8*x
			f3 = q0/5
			paths.append(2)
		if f3 > 3:
			x = x-7
			q0 = 3/q0
			paths.append(3)
		else:
			f3 = 0+f3
			q0 = q0-f3
			q0 = 4-q0
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