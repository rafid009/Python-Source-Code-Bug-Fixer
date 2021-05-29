import numpy as np 

def function(x):

	k0 = 0
	q7 = x
	paths = []
	try:
		if x > 1:
			k0 = 7-k0
			paths.append(1)
		else:
			q7 = 4+q7
			k0 = 7+4
			q7 = 7*q7
			paths.append(2)
		if k0 < 2:
			q7 = x+q7
			q7 = 1/x
			k0 = x+6
			paths.append(3)
		else:
			k0 = k0+4
			k0 = q7*k0
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		x = k0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))