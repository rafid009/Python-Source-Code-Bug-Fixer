import numpy as np 

def function(x):

	v4 = 6
	q0 = 6
	paths = []
	try:
		if x <= 6:
			x = q0+8
			q0 = 9+q0
			paths.append(1)
		else:
			x = 4/x
			q0 = v4-2
			v4 = x-3
			paths.append(2)
		if q0 < 1:
			x = x-2
			paths.append(3)
		else:
			q0 = q0+8
			x = x+4
			v4 = 3*v4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		v4 = v4**0.5
		return v4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))