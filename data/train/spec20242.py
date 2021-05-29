import numpy as np 

def function(x):

	v2 = x
	q0 = x
	paths = []
	try:
		if q0 > 1:
			x = 3+4
			x = 1/3
			paths.append(1)
		else:
			x = q0/q0
			x = x-1
			v2 = v2*5
			paths.append(2)
		if q0 >= 8:
			v2 = 8+2
			paths.append(3)
		else:
			v2 = 6+1
			v2 = 2*v2
			v2 = 5+9
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		v2 = q0**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))