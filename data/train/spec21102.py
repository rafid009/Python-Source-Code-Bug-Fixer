import numpy as np 

def function(x):

	w6 = x
	q0 = x
	x = 4
	paths = []
	try:
		if q0 > 2:
			x = 7*q0
			paths.append(1)
		else:
			w6 = 5/8
			x = 7/4
			x = x/q0
			paths.append(2)
		if w6 >= 3:
			x = x*8
			q0 = 3+q0
			q0 = 2+q0
			paths.append(3)
		else:
			w6 = 4*q0
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