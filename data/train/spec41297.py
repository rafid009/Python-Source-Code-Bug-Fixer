import numpy as np 

def function(x):

	k2 = 3
	r3 = 9
	paths = []
	try:
		if r3 < 6:
			r3 = r3+k2
			x = x/k2
			paths.append(1)
		else:
			k2 = 5+k2
			r3 = r3-8
			r3 = x/r3
			paths.append(2)
		if r3 <= 9:
			r3 = r3+4
			paths.append(3)
		else:
			x = 3+x
			r3 = r3+6
			k2 = 8/k2
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