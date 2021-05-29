import numpy as np 

def function(x):

	q0 = x
	w9 = 2
	paths = []
	try:
		if q0 >= 1:
			x = 3/x
			w9 = 4/w9
			q0 = q0+2
			paths.append(1)
		else:
			x = 1*q0
			w9 = x*w9
			q0 = q0+0
			paths.append(2)
		if x >= 7:
			x = 6+w9
			paths.append(3)
		else:
			q0 = q0/6
			q0 = 3/q0
			x = x-2
			paths.append(4)
		paths.append(5)
		assert w9 >= 0
		x = w9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))