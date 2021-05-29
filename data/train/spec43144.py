import numpy as np 

def function(x):

	q0 = x
	k1 = 3
	paths = []
	try:
		if x > 6:
			q0 = k1/q0
			x = x*2
			paths.append(1)
		else:
			x = x/x
			x = k1+k1
			q0 = q0+3
			paths.append(2)
		if q0 >= 2:
			k1 = x/3
			q0 = q0+6
			x = x/q0
			paths.append(3)
		else:
			x = 6-3
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