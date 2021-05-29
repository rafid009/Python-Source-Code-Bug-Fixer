import numpy as np 

def function(x):

	k0 = x
	q2 = 5
	paths = []
	try:
		if k0 < 7:
			q2 = q2-4
			q2 = x/5
			paths.append(1)
		else:
			x = 1-x
			k0 = k0/5
			q2 = q2-x
			paths.append(2)
		if k0 < 4:
			q2 = 0*5
			paths.append(3)
		else:
			q2 = 8-q2
			x = x*5
			paths.append(4)
		paths.append(5)
		assert q2 >= 0
		x = q2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))