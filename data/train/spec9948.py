import numpy as np 

def function(x):

	k2 = 1
	r3 = x
	x = 1
	paths = []
	try:
		if r3 >= 2:
			r3 = r3+5
			paths.append(1)
		else:
			k2 = x/6
			k2 = k2-4
			paths.append(2)
		if k2 < 7:
			r3 = r3+r3
			k2 = k2/r3
			paths.append(3)
		else:
			k2 = 0/k2
			x = 3/x
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		x = k2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))